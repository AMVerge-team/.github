#!/usr/bin/env python3
"""Generate animated RGB AMVerge banners matching AMVerge-CLI.gif.

Usage:
    python3 scripts/generate-banners.py --all
    python3 scripts/generate-banners.py Scoop
    python3 scripts/generate-banners.py "Android" "Docs"
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "assets" / "banners" / "src"
OUT_DIR = ROOT / "assets" / "banners"
BASE_GIF = SRC_DIR / "amverge_title_gif.gif"
FONT_FILE = SRC_DIR / "Jersey10-Regular.ttf"

DEFAULT_SUFFIXES = [
    "Team",
    "CLI",
    "Website",
    "Extension",
    "iOS",
    "Android",
    "Bot",
    "Homebrew",
    "Scoop",
    "Models",
    "Admin",
]


def safe_filename(suffix: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", suffix.strip()).strip("-")
    return f"AMVerge-{cleaned}.gif"


def generate_banner(suffix: str) -> Path:
    src = Image.open(BASE_GIF)
    w, h = src.size
    border = 8

    f0 = src.convert("RGBA")
    inner = f0.crop((border, border, w - border, h - border))
    bbox = inner.convert("L").point(lambda p: 255 if p > 10 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("Could not detect AMVerge logo bounding box in base GIF.")
    lx, ly, rx, ry = bbox[0] + border, bbox[1] + border, bbox[2] + border, bbox[3] + border
    logo_w = rx - lx

    font = ImageFont.truetype(str(FONT_FILE), 225)
    tb = font.getbbox(suffix)
    tw = tb[2] - tb[0]
    gap = 42
    start_x = (w - (logo_w + gap + tw)) // 2
    text_y = ly - tb[1] + 5

    frames: list[Image.Image] = []
    for i in range(src.n_frames):
        src.seek(i)
        fr = src.convert("RGBA")
        out = fr.copy()
        draw = ImageDraw.Draw(out)
        draw.rectangle([border, border, w - border - 1, h - border - 1], fill=(0, 0, 0, 255))
        out.paste(fr.crop((lx, ly, rx, ry)), (start_x, ly))
        draw.text((start_x + logo_w + gap - tb[0], text_y), suffix, font=font, fill=(255, 255, 255, 255))
        frames.append(out.convert("P", palette=Image.ADAPTIVE, colors=64))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / safe_filename(suffix)
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=src.info.get("duration", 50),
        loop=0,
        optimize=True,
    )
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate animated RGB AMVerge banners.")
    parser.add_argument("suffixes", nargs="*", help="One or more suffix labels (e.g. Scoop, iOS, Website)")
    parser.add_argument("--all", action="store_true", help="Generate all default org banners")
    args = parser.parse_args()

    targets = DEFAULT_SUFFIXES if args.all or not args.suffixes else args.suffixes
    for suffix in targets:
        out = generate_banner(suffix)
        size_kb = out.stat().st_size / 1024
        print(f"Generated {out.relative_to(ROOT)} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()

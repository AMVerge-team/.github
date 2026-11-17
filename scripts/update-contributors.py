import json
import os
import re
import urllib.error
import urllib.request

ORG = "AMVerge-team"
README_PATH = "profile/README.md"
EXCLUDE = {"moongetsu", "crptk"}
PER_ROW = 7

TOKEN = os.environ.get("GITHUB_TOKEN")
HEADERS = {
    "User-Agent": "AMVerge-Contributors-Action",
    "Accept": "application/vnd.github+json",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def fetch_paginated(base_url: str) -> list[dict]:
    items: list[dict] = []
    page = 1
    while True:
        sep = "&" if "?" in base_url else "?"
        url = f"{base_url}{sep}per_page=100&page={page}"
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status == 204:
                    break
                raw = resp.read().decode("utf-8")
                if not raw.strip():
                    break
                batch = json.loads(raw)
        except urllib.error.HTTPError as exc:
            if exc.code in (204, 404):
                break
            raise
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


def main() -> None:
    repos = fetch_paginated(f"https://api.github.com/orgs/{ORG}/repos?type=public")
    by_login: dict[str, dict] = {}

    for repo in repos:
        if repo.get("archived"):
            continue
        contribs = fetch_paginated(repo["contributors_url"])
        for c in contribs:
            login = c.get("login", "")
            if (
                not login
                or login.lower() in EXCLUDE
                or login.endswith("[bot]")
                or c.get("type") == "Bot"
            ):
                continue
            key = login.lower()
            if key not in by_login:
                by_login[key] = {
                    "login": login,
                    "html_url": c["html_url"],
                    "avatar_url": c["avatar_url"],
                    "contributions": 0,
                }
            by_login[key]["contributions"] += c.get("contributions", 0)

    filtered = sorted(
        by_login.values(),
        key=lambda c: (-c["contributions"], c["login"].lower()),
    )

    rows = []
    for i in range(0, len(filtered), PER_ROW):
        cells = []
        for c in filtered[i : i + PER_ROW]:
            avatar = c["avatar_url"]
            sep = "&" if "?" in avatar else "?"
            cells.append(
                "<td>"
                f'<a href="{c["html_url"]}">'
                f'<img src="{avatar}{sep}s=64" width="64" '
                f'style="border-radius: 4px;" loading="lazy" alt="{c["login"]}" />'
                f"<br/><sub>{c['login']}</sub>"
                "</a>"
                "</td>"
            )
        rows.append("  <tr>\n    " + "\n    ".join(cells) + "\n  </tr>")

    table = '<table align="center">\n' + "\n".join(rows) + "\n</table>"

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"<!-- CONTRIBUTORS-START -->.*<!-- CONTRIBUTORS-END -->",
        f"<!-- CONTRIBUTORS-START -->\n\n{table}\n\n<!-- CONTRIBUTORS-END -->",
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated README with {len(filtered)} contributors across {len(repos)} repos")


if __name__ == "__main__":
    main()

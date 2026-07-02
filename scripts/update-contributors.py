import json
import os
import re
import urllib.request

REPO = "AMVerge-team/AMVerge"
README_PATH = "profile/README.md"
EXCLUDE = {"moongetsu", "crptk"}
PER_ROW = 7

url = f"https://api.github.com/repos/{REPO}/contributors?per_page=100"

token = os.environ.get("GITHUB_TOKEN")
headers = {"User-Agent": "AMVerge-Contributors-Action"}
if token:
    headers["Authorization"] = f"Bearer {token}"

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    contributors = json.loads(resp.read())

filtered = [
    c
    for c in contributors
    if c["login"].lower() not in EXCLUDE
    and not c["login"].endswith("[bot]")
    and c.get("type") != "Bot"
]

rows = []
for i in range(0, len(filtered), PER_ROW):
    cells = []
    for c in filtered[i : i + PER_ROW]:
        cells.append(
            "<td>"
            f'<a href="{c["html_url"]}">'
            f'<img src="{c["avatar_url"]}&s=64" width="64" '
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

print(f"Updated README with {len(filtered)} contributors")

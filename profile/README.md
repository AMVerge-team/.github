<div align="center">

<img src="https://raw.githubusercontent.com/AMVerge-team/AMVerge/main/frontend/src/assets/amverge_title_gif.gif" width="100%" alt="AMVerge" />

### Open-source tools for AMV editors

Scene selection made easy. Built for the AMV community, by editors, for editors.

<br/>

[![GitHub Org](https://img.shields.io/badge/org-AMVerge%20Team-22c55e?style=for-the-badge&logo=github&logoColor=white&labelColor=0d2818)](https://github.com/AMVerge-team)
[![PyPI](https://img.shields.io/badge/pypi-amverge-22c55e?style=for-the-badge&logo=pypi&logoColor=white&labelColor=0d2818)](https://pypi.org/project/amverge/)
[![Website](https://img.shields.io/badge/site-amverge.app-22c55e?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0d2818)](https://amverge.app)

</div>

---


<div align="center">

## Projects

</div>
<br/>
<table>
<tr>
<td width="50%" valign="top" align="center">

<p align="center">
  <img src="https://raw.githubusercontent.com/moongetsu/AMVerge-Website/refs/heads/AMVergeV2/public/LogoAMVerge.png" width="48" style="border-radius: 4px; overflow: hidden;" />
</p>

### [AMVerge](https://github.com/AMVerge-team/AMVerge)

Desktop scene selection app. ML-powered detection, visual clip browser, smart merge, multi-format export. Tauri + React + Python.

[![Release](https://img.shields.io/github/v/release/AMVerge-team/AMVerge?style=flat-square&label=latest&color=22c55e&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/AMVerge-team/AMVerge/total?style=flat-square&label=downloads&color=16a34a&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/releases)
[![License](https://img.shields.io/badge/license-GPL--3.0-22c55e?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/blob/main/LICENSE)

</td>
<td width="50%" valign="top" align="center">

<p align="center">
  <img src="https://skillicons.dev/icons?i=python&theme=dark" width="48" style="border-radius: 4px; overflow: hidden;" />
</p>

### [AMVerge CLI](https://github.com/AMVerge-team/AMVerge-CLI)

Standalone Python CLI and library. Full backend port. Scene detection, AI upscaling, frame interpolation, smart cutting. `pip install amverge`.

[![PyPI](https://img.shields.io/pypi/v/amverge?style=flat-square&label=pypi&color=22c55e&labelColor=0d2818)](https://pypi.org/project/amverge/)
[![Python](https://img.shields.io/badge/python-3.11+-blue?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-CLI)
[![License](https://img.shields.io/badge/license-GPL--3.0-22c55e?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-CLI/blob/main/LICENSE)

</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f310.png" width="48" style="border-radius: 4px; overflow: hidden;" />
</p>

### [AMVerge Website](https://github.com/AMVerge-team/AMVerge-Website)

Marketing landing page and docs. React 19, TypeScript, Vite 8, MDX. Live changelog from GitHub releases, FAQ, feature showcase.

[![Site](https://img.shields.io/badge/site-amverge.app-22c55e?style=flat-square&logo=vercel&logoColor=white&labelColor=0d2818)](https://amverge.app)
[![Stack](https://img.shields.io/badge/stack-React%2019%20%2B%20Vite%208-61dafb?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-Website)
[![License](https://img.shields.io/badge/license-GPL--3.0-22c55e?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-Website/blob/main/LICENSE)

</td>
<td width="50%" valign="top" align="center">
<br/>
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Adobe_After_Effects_CC_2026_icon.svg/1280px-Adobe_After_Effects_CC_2026_icon.svg.png" width="48" style="border-radius: 4px; overflow: hidden;" />
</p>

### [AMVerge Extension](https://github.com/AMVerge-team/AMVerge-Extension)

After Effects extension for the AMVerge ecosystem. Coming soon.

[![Repo](https://img.shields.io/badge/view-repo-22c55e?style=flat-square&logo=github&logoColor=white&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-Extension)

</td>
</tr>
</table>

---

<br/>

## CLI at a Glance

```bash
pip install amverge
```

```bash
amverge detect episode.mp4 --method transnet
amverge export episode.mp4 --scenes scenes.json --select 0,2,5-8
amverge upscale episode.mp4 --method ml --model adore -s 2
amverge interpolate episode.mp4 -f 2
amverge merge clip1.mp4 clip2.mp4 --output out.mp4
```

- **Scene detection** : TransNetV2 ML · keyframe · edge
- **AI upscaling** : ShuffleCUGAN · Anime4K · ArtCNN
- **Frame interpolation** : RIFE PyTorch · Flowframes
- **Smart cutting** : Lossless copy · smartcut · re-encode
- **Export** : 15 codec profiles · 10 audio codecs · MP4/MKV/MOV
- **Utilities** : Thumbnails · duplicate detection · metadata inspection · Discord RPC

---
<br/>
<div align="center">

## Languages & Frameworks
<img src="https://skillicons.dev/icons?i=python,typescript,react,tauri,rust,vite,pytorch,nodejs,bash&theme=dark&perline=9" alt="Tech Stack" />

## Team

<table border="0" cellspacing="0" cellpadding="10">
  <tr>
    <td align="center" valign="top">
      <img src="https://github.com/crptk.png" width="72" style="border-radius: 4px; overflow: hidden;" /><br/>
      <strong><a href="https://github.com/crptk">Crptk</a></strong><br/>
      Creator
    </td>
    <td align="center" valign="top">
      <img src="https://github.com/Moongetsu.png" width="72" style="border-radius: 4px; overflow: hidden;" /><br/>
      <strong><a href="https://github.com/Moongetsu">Moongetsu</a></strong><br/>
      Maintainer
    </td>
  </tr>
</table>

<br/>

## Thank You

AMVerge wouldn't exist without you.

<!-- CONTRIBUTORS-START -->
<!-- CONTRIBUTORS-END -->

<br/>

&copy; 2026 AMVerge. All rights reserved.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:0d2818,100:0d3320&height=100&section=footer" width="100%" />

</div>

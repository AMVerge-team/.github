<div align="center">

<img src="https://raw.githubusercontent.com/AMVerge-team/AMVerge/main/frontend/src/assets/amverge_title_gif.gif" width="100%" alt="AMVerge" />

### Open-source tools for AMV & video editors

Scene splitting, semantic scene search, and AI post-processing made effortless. Built by editors, for editors.

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

Desktop scene-splitting & clip curation app. `TransNetV2` detection, **Scene Scout** (SigLIP 2 semantic & visual search), AI depth maps & upscaling, scenepacks, and direct send to AE, Premiere, Resolve & CapCut. Tauri + React + Python.

[![Release](https://img.shields.io/github/v/release/AMVerge-team/AMVerge?style=flat-square&label=latest&color=22c55e&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/AMVerge-team/AMVerge/total?style=flat-square&label=downloads&color=16a34a&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/releases)
[![Stars](https://img.shields.io/github/stars/AMVerge-team/AMVerge?style=flat-square&color=22c55e&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/stargazers)
[![License](https://img.shields.io/badge/license-GPL--3.0-22c55e?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge/blob/main/LICENSE)

</td>
<td width="50%" valign="top" align="center">

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Bash_Logo_Colored.svg/960px-Bash_Logo_Colored.svg.png" width="48" style="border-radius: 4px; overflow: hidden;" />
</p>

### [AMVerge CLI](https://github.com/AMVerge-team/AMVerge-CLI)

Standalone Python CLI and library (`import amverge`). Full backend port with scene detection, AI upscaling, RIFE/Flowframes interpolation, Depth-Anything-V2 depth maps, deadframe removal, and chained pipelines.

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

Landing page, interactive showcase, and documentation. React 19, TypeScript, Vite 8, MDX. Live release changelogs, download counters, FAQ, and feature walkthroughs.

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

After Effects CEP extension (CC 2018–2026+ on Windows). Detect scene cuts via Keyframe, Edge, or TransNetV2, preview clip thumbnails, and batch-import straight into your composition as auto-scaled layers.

[![Release](https://img.shields.io/github/v/release/AMVerge-team/AMVerge-Extension?style=flat-square&label=latest&color=22c55e&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-Extension/releases/latest)
[![After Effects](https://img.shields.io/badge/After%20Effects-CC%202018--2026%2B-9999ff?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-Extension)
[![License](https://img.shields.io/badge/license-MIT-22c55e?style=flat-square&labelColor=0d2818)](https://github.com/AMVerge-team/AMVerge-Extension/blob/main/LICENSE)

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
amverge depth episode.mp4
amverge pipeline episode.mp4
amverge merge clip1.mp4 clip2.mp4 --output out.mp4
```

- **Scene detection**: TransNetV2 ML · keyframe · Canny edge
- **Semantic search (Desktop)**: Scene Scout via SigLIP 2 text search & Flow visual matching
- **AI upscaling**: ShuffleCUGAN (ML) · Anime4K (shaders) · ArtCNN (ONNX)
- **Frame interpolation**: RIFE PyTorch (CUDA/CPU) · Flowframes
- **Depth & cleanup**: Depth-Anything-V2 monocular depth maps · optical-flow deadframe removal · chained pipelines
- **Smart cutting & export**: Lossless copy · smartcut · 15 codec profiles (NVENC/AMF/QSV/VAAPI) · 10 audio codecs · MP4/MOV/AVI
- **Ecosystem & utilities**: Thumbnails · duplicate detection · metadata inspection · `import amverge` Python API · Discord RPC

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

<table align="center">
  <tr>
    <td><a href="https://github.com/NetsumaInfo"><img src="https://avatars.githubusercontent.com/u/125161702?v=4&s=64" width="64" style="border-radius: 4px;" loading="lazy" alt="NetsumaInfo" /><br/><sub>NetsumaInfo</sub></a></td>
    <td><a href="https://github.com/ligatima"><img src="https://avatars.githubusercontent.com/u/280236744?v=4&s=64" width="64" style="border-radius: 4px;" loading="lazy" alt="ligatima" /><br/><sub>ligatima</sub></a></td>
    <td><a href="https://github.com/Mark-Shun"><img src="https://avatars.githubusercontent.com/u/57092443?v=4&s=64" width="64" style="border-radius: 4px;" loading="lazy" alt="Mark-Shun" /><br/><sub>Mark-Shun</sub></a></td>
    <td><a href="https://github.com/TOSINIRL"><img src="https://avatars.githubusercontent.com/u/247466584?v=4&s=64" width="64" style="border-radius: 4px;" loading="lazy" alt="TOSINIRL" /><br/><sub>TOSINIRL</sub></a></td>
    <td><a href="https://github.com/nuruodo"><img src="https://avatars.githubusercontent.com/u/158218912?v=4&s=64" width="64" style="border-radius: 4px;" loading="lazy" alt="nuruodo" /><br/><sub>nuruodo</sub></a></td>
  </tr>
</table>

<!-- CONTRIBUTORS-END -->

<br/>

&copy; 2026 AMVerge. All rights reserved.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:0d2818,100:0d3320&height=100&section=footer" width="100%" />

</div>

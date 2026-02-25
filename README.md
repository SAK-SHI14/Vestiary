<div align="center">

<img src="https://img.shields.io/badge/Vestiary-v1.0.0-blueviolet?style=for-the-badge&logo=sparkles" alt="Vestiary Version"/>

# 👗 Vestiary — AI-Powered Personal Stylist

**An intelligent, production-ready fashion recommendation engine that crafts personalized outfit suggestions by occasion, weather, style preference, and color palette — powered by AI image upscaling and a premium glassmorphism UI.**

<br/>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenCV](https://img.shields.io/badge/OpenCV-DNN_SuperRes-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Engine-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle_Fashion-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/SAK-SHI14/Vestiary?style=flat-square&color=F59E0B)](https://github.com/SAK-SHI14/Vestiary/stargazers)

<br/>

> *"Your wardrobe, reimagined by intelligence."*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Quick Start](#-quick-start)
  - [Local Setup](#local-setup)
  - [Docker Deployment](#docker-deployment)
- [AI Upscaling Engine](#-ai-upscaling-engine)
  - [Production-Grade Super Resolution](#production-grade-super-resolution-edsr)
  - [Fallback: Bicubic + Unsharp Mask](#fallback-bicubic--unsharp-mask-pipeline)
- [How It Works](#-how-it-works)
- [UI/UX Design Philosophy](#-uiux-design-philosophy)
- [Configuration & Filters](#-configuration--filters)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Vestiary** is a full-stack AI fashion recommendation system built with a production-first mindset. It bridges the gap between raw fashion data and intelligent personal styling by leveraging:

- **Multi-attribute filtering**: gender, occasion, season, color palette, and weather compatibility
- **AI-powered image enhancement**: EDSR Deep Neural Network super-resolution to present every outfit at its best
- **Premium glassmorphism UI**: a carefully crafted aesthetic that feels like a luxury fashion portal

Born from the [Kaggle Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset), Vestiary transforms a flat CSV of product metadata into a dynamic, visually rich, and highly personalized styling experience.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| 🎯 **Smart Outfit Filtering** | Multi-dimensional filtering by gender, occasion, color group, and weather compatibility |
| 🌈 **Hex Color Matching** | Pick any color using the color picker; Vestiary resolves the nearest CSS3 color name and matches dataset entries |
| 🖼️ **AI Image Upscaling** | EDSR DNN Super-Resolution model (4× upscale) with a graceful fallback to bicubic + unsharp mask |
| 🧩 **Modular Architecture** | Clean separation of data ingestion, recommendation logic, UI/styling, and utility functions |
| 💎 **Premium Glassmorphism UI** | Backdrop blur, gradient cards, masonry-style grid, and a refined "Vestiary" aesthetic |
| 🐳 **Docker-Ready** | One-command containerized deployment for cloud platforms (AWS, GCP, Azure, Render) |
| 📊 **Interactive Sidebar** | Real-time filter controls with live result count updates |
| 🗃️ **Script-Assisted Data Pipeline** | Dedicated script to download the full high-resolution dataset from Kaggle |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE (Streamlit)                  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  Sidebar Controls          │  Main Display Grid               │  │
│  │  ┌──────────────────────┐  │  ┌─────────────────────────────┐│  │
│  │  │ • Gender Selector     │  │  │ Masonry-style Outfit Cards  ││  │
│  │  │ • Occasion Picker    │  │  │  ┌──────┐ ┌──────┐ ┌─────┐ ││  │
│  │  │ • Weather Mode       │  │  │  │ Card │ │ Card │ │ ... │ ││  │
│  │  │ • Color Picker       │  │  │  └──────┘ └──────┘ └─────┘ ││  │
│  │  │ • Advanced Filters   │  │  └─────────────────────────────┘│  │
│  │  └──────────────────────┘  │                                  │  │
│  └───────────────────────────────────────────────────────────────┘  │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
              ┌─────────────────▼──────────────────┐
              │           app.py (Entry Point)       │
              └───┬──────────┬───────────┬──────────┘
                  │          │           │
       ┌──────────▼──┐  ┌────▼─────┐  ┌────▼─────┐   ┌─────────────┐
       │ data_loader │  │recommender│  │  styles  │   │    utils    │
       │    .py      │  │   .py     │  │   .py    │   │    .py      │
       │  ─────────  │  │ ────────  │  │ ───────  │   │ ──────────  │
       │CSV ingestion│  │ Filtering │  │ CSS/HTML │   │ AI Upscaler │
       │Path mapping │  │  Engine   │  │  Inject  │   │ (EDSR/DNN)  │
       │ Validation  │  │Color Match│  │   Glass  │   │  Bicubic    │
       └─────────────┘  └──────────┘  └──────────┘   └─────────────┘
                                │
              ┌─────────────────▼──────────────────┐
              │           Data Layer                 │
              │   styles.csv  │  images/  │ EDSR.pb  │
              └─────────────────────────────────────┘
```

---

## 📂 Project Structure

```
Vestiary/
│
├── app.py                        # 🚪 Main Streamlit entry point
├── Dockerfile                    # 🐳 Container build configuration
├── requirements.txt              # 📦 Python dependencies
├── EDSR_x4.pb                   # 🧠 EDSR Super-Resolution model weights
│
├── src/                          # 📁 Core application modules
│   ├── data_loader.py            #    CSV ingestion, path resolution, validation
│   ├── recommender.py            #    Multi-attribute filtering + color matching engine
│   ├── styles.py                 #    Glassmorphism CSS, custom HTML components
│   └── utils.py                  #    AI upscaler (EDSR DNN + bicubic fallback)
│
├── scripts/                      # 🛠️ Utility scripts
│   └── download_data.py          #    Kaggle dataset downloader (high-res, ~15GB)
│
├── images/                       # 🖼️ Fashion product image thumbnails
│   └── images/
│       └── *.jpg                 #    Individual product images (by product ID)
│
├── styles.csv                    # 📊 Primary fashion dataset (44k+ products)
├── images.csv                    # 🗂️ Image metadata index
├── styles dataset.ipynb          # 📓 EDA & data preprocessing notebook
│
├── debug_images.py               # 🔍 Internal debug utility for image paths
├── debug_log.txt                 # 📋 Debug output log
└── .gitignore                    # 🚫 VCS ignore rules
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | [Streamlit 1.28+](https://streamlit.io) | Interactive web UI with custom CSS injection |
| **Data Engine** | [Pandas](https://pandas.pydata.org) | DataFrame operations, filtering, CSV I/O |
| **AI Vision** | [OpenCV DNN](https://opencv.org) | EDSR Super-Resolution + bicubic upscaling |
| **Color Mapping** | [webcolors](https://webcolors.readthedocs.io) | Hex → CSS3 color name resolution |
| **Visualization** | [Matplotlib](https://matplotlib.org) | Supporting visualizations |
| **Containerization** | [Docker](https://docker.com) | Reproducible, cloud-ready deployment |
| **Dataset Source** | [Kaggle Fashion Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset) | 44k+ fashion products with metadata |
| **Language** | Python 3.9+ | Application runtime |

---

## 📊 Dataset

Vestiary is powered by the **Kaggle Fashion Product Images Dataset** (by Param Aggarwal), a comprehensive catalog of `44,446` fashion products.

**Dataset Schema (`styles.csv`)**:

| Column | Type | Description |
|---|---|---|
| `id` | int | Unique product identifier |
| `gender` | str | Target gender (`Men`, `Women`, `Boys`, `Girls`, `Unisex`) |
| `masterCategory` | str | Top-level category (`Apparel`, `Footwear`, etc.) |
| `subCategory` | str | Sub-level category (`Topwear`, `Bottomwear`, etc.) |
| `articleType` | str | Specific article type (`T-Shirt`, `Jeans`, etc.) |
| `baseColour` | str | Primary product color |
| `season` | str | Seasonal tag (`Summer`, `Winter`, `Fall`, `Spring`) |
| `year` | int | Year of listing |
| `usage` | str | Occasion tag (`Casual`, `Formal`, `Sports`, etc.) |
| `productDisplayName` | str | Full product name |

> **Note**: The local dataset includes enriched columns like `color_group` and `weather_compatibility`, added during the preprocessing phase (see `styles dataset.ipynb`).

---

## ⚡ Quick Start

### Prerequisites

- Python 3.9 or higher
- `pip` package manager
- (Optional) Docker for containerized deployment
- (Optional) Kaggle API key for full high-resolution dataset download

---

### Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/SAK-SHI14/Vestiary.git
cd Vestiary
```

**2. (Recommended) Create a virtual environment**
```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Verify dataset files are present**

Ensure the following files exist in the project root:
```
Vestiary/
├── styles.csv          ✅ Required
└── images/
    └── images/
        └── *.jpg       ✅ Required (fashion product images)
```

> If images are missing, use the data downloader script (see [Dataset Download](#dataset-download-optional)).

**5. Run the application**
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501** 🎉

---

### Dataset Download (Optional)

To download the full 15GB high-resolution dataset from Kaggle:

```bash
# Configure your Kaggle API key first:
# Place kaggle.json at ~/.kaggle/kaggle.json (Linux/macOS)
# or C:\Users\<username>\.kaggle\kaggle.json (Windows)

python scripts/download_data.py
```

Follow the on-screen prompts. Once downloaded, copy the contents of the `high_res_data/fashion-product-images-dataset/.../images/` folder into `images/images/`.

---

### Docker Deployment

**1. Build the Docker image**
```bash
docker build -t vestiary:latest .
```

**2. Run the container**
```bash
docker run -p 8501:8501 vestiary:latest
```

**3. Access the application**
```
http://localhost:8501
```

**For cloud deployment (e.g., Render, Railway, AWS ECS)**, the image is self-contained and uses port `8501`. Set the `PORT` environment variable if your cloud provider requires it.

---

## 🧠 AI Upscaling Engine

Vestiary features a dual-mode image enhancement pipeline implemented in `src/utils.py` using a **Singleton pattern** to ensure the heavy model is loaded only once.

### Production-Grade Super-Resolution (EDSR)

When `EDSR_x4.pb` is present in the project root, Vestiary uses **Enhanced Deep Residual Networks for Single Image Super-Resolution** — a state-of-the-art DNN model that performs true **4× upscale** via learned convolutional filters.

```python
# Automatic model detection and loading (singleton)
model_path = "EDSR_x4.pb"
if os.path.exists(model_path):
    sr.readModel(model_path)
    sr.setModel("edsr", 4)  # 4x upscaling factor
```

> The `EDSR_x4.pb` model file (~38MB) is included in the repository for convenience.

---

### Fallback: Bicubic + Unsharp Mask Pipeline

When the EDSR model is unavailable, the system falls back to a classical computer vision pipeline:

```
Input Image (60×80px thumbnail)
        │
        ▼
[cv2.INTER_CUBIC] ──→ 4× resize (240×320px)
        │
        ▼
[GaussianBlur σ=2.0] ──→ Smoothed copy
        │
        ▼
[addWeighted: 1.5×sharp − 0.5×smooth] ──→ Unsharp Mask Sharpening
        │
        ▼
Enhanced Output (cleaner, sharper thumbnail)
```

---

## 🔍 How It Works

The recommendation pipeline in `src/recommender.py` executes a sequential filter chain on the `styles.csv` dataset:

```
User Inputs
    │
    ├── Gender Selection
    │     └── Maps: Female → [women, girls, unisex]
    │               Male   → [men, boys, unisex]
    │
    ├── Occasion Filter
    │     └── Case-insensitive substring match on `usage` column
    │
    ├── Color Group Filter
    │     └── Exact match on enriched `color_group` column
    │         (warm / cool / neutral / bright / natural)
    │
    ├── Weather Filter
    │     └── Maps weather → compatible dataset tags
    │         hot   → [hot, any, cool]
    │         cold  → [cold]
    │         rainy → [rainy]
    │
    ├── Advanced Weather Compatibility
    │     └── Exact match on `weather_compatibility` column
    │
    └── Color Picker → HEX → CSS3 Color Name (webcolors)
          └── Used for display; color matching via Euclidean distance in RGB space
```

**Result**: A filtered `DataFrame` of up to **40 matching outfits**, rendered in a 4-column masonry grid with AI-enhanced images and product metadata.

---

## 🎨 UI/UX Design Philosophy

Vestiary's interface (`src/styles.py`) is built around three design principles:

1. **Glassmorphism**: Semi-transparent cards with `backdrop-filter: blur()`, subtle borders, and layered depth
2. **Refined Color Palette**: Deep navy backgrounds (`#0d0d1a`), violet-to-pink gradients, and gold accent tones
3. **Micro-interactions**: Hover lift effects, smooth transitions on cards, and animated gradient headers

All styles are injected via Streamlit's `st.markdown(..., unsafe_allow_html=True)` mechanism, bypassing default Streamlit theming for a fully custom aesthetic.

---

## ⚙️ Configuration & Filters

Vestiary exposes the following configuration options through its sidebar:

| Filter | Options | Default |
|---|---|---|
| **Gender** | Female, Male, Unisex | Female |
| **Occasion** | Casual, Formal, Sports, Ethnic, Travel, … | (Dataset-driven) |
| **Current Weather** | Hot, Cold, Rainy, Any | Any |
| **Accent Color** | Any HEX color (color picker) | `#D4AF37` (Gold) |
| **Color Tone** (Advanced) | Any, Warm, Cool, Neutral, Bright, Natural | Any |
| **Weather Compatibility** (Advanced) | Any, Hot, Cold, Cool, Rainy | Any |

All occasion values are **dynamically loaded** from the unique `usage` values present in `styles.csv`, ensuring the UI stays in sync with the dataset.

---

## 🛣️ Roadmap

- [ ] **v1.1** — Add full-text search across product names
- [ ] **v1.2** — User favorites / saved collections (session state)
- [ ] **v1.3** — Complete outfit builder (top + bottom + accessory combos)
- [ ] **v1.4** — Integrate a real-time weather API for auto-detection
- [ ] **v2.0** — Deep learning–based visual similarity search (CLIP / ResNet embeddings)
- [ ] **v2.0** — User account system with personalized style profiles
- [ ] **v3.0** — Virtual try-on integration (Diffusion model–powered)

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get started:

1. **Fork** the repository
2. **Create** your feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'feat: add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and ensure your code is documented.

For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Developed with ❤️ by [Sakshi Verma](https://github.com/SAK-SHI14)**

*If you found this project useful, please consider giving it a ⭐ — it means a lot!*

[![GitHub Stars](https://img.shields.io/github/stars/SAK-SHI14/Vestiary?style=social)](https://github.com/SAK-SHI14/Vestiary/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/SAK-SHI14/Vestiary?style=social)](https://github.com/SAK-SHI14/Vestiary/network/members)

</div>

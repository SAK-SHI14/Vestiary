# ✨ AI Recommendation App (Vestiary)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b)
![OpenCV](https://img.shields.io/badge/OpenCV-DNN-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

A premium, industry-ready fashion recommendation system powered by AI. This application suggests outfits based on gender, occasion, weather, and color preferences, featuring a high-end user interface and on-the-fly image upscaling.

## 🚀 Features

-   **Modular Architecture**: Clean separation of concerns (Data, Logic, UI) for maintainability and scalability.
-   **AI Image Upscaling**: Integrates OpenCV DNN Super Resolution to enhance low-quality dataset images using EDSR/FSRCNN models.
-   **Smart Filtering**: Advanced logic to match outfits with weather conditions and color moods.
-   **Premium UI**: Glassmorphism effects, responsive masonry grid, and a refined "Vestiary" aesthetic.
-   **Containerized**: Includes a `Dockerfile` for easy deployment to cloud platforms (AWS, GCP, Azure).

## 📂 Project Structure

```
├── app.py                  # Main Entry Point
├── Dockerfile              # Container Configuration
├── requirements.txt        # Dependencies
├── src/
│   ├── data_loader.py      # Robust Data Ingestion
│   ├── recommender.py      # Core Recommendation Engine
│   ├── styles.py           # UI/UX & CSS Components
│   └── utils.py            # AI Helper Utilities (Upscaling)
└── styles.csv              # Fashion Dataset
```

## 🛠️ Installation & Setup

### Local Method
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/SAK-SHI14/Vestiary.git
    cd Vestiary
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

### Docker Method
1.  **Build the image**:
    ```bash
    docker build -t ai-recommendation-app .
    ```
2.  **Run the container**:
    ```bash
    docker run -p 8501:8501 ai-recommendation-app
    ```

## 🧠 AI Upscaling Note
The project handles low-resolution thumbnails by applying basic bicubic upscaling by default. for production-grade super-resolution:
1.  Download the `EDSR_x4.pb` model.
2.  Place it in the root directory.
3.  The `Upscaler` class in `src/utils.py` will automatically detect and use it.

## 🤝 Contributing
Contributions are welcome! Please follow the standard fork-and-pull-request workflow.

---
*Developed by Sakshi Verma*

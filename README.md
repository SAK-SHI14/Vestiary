<br/>
<div align="center">
  <h1 align="center">Vestiary ✨</h1>
  <p align="center">
    <strong>An Enterprise-Grade AI Fashion Stylist & Virtual Try-On Platform</strong>
    <br/>
    <br/>
    <a href="https://github.com/SAK-SHI14/Vestiary/issues">Report Bug</a>
    ·
    <a href="https://github.com/SAK-SHI14/Vestiary/issues">Request Feature</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
    <img src="https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E" alt="Vite" />
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#core-capabilities">Core Capabilities</a></li>
        <li><a href="#tech-stack">Tech Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation-and-setup">Installation and Setup</a></li>
      </ul>
    </li>
    <li><a href="#system-architecture">System Architecture</a></li>
    <li><a href="#api-reference">API Reference</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<hr/>

## About The Project

**Vestiary** is a cutting-edge, AI-powered fashion recommendation and styling web application designed to bridge the gap between imagination and reality in personal styling. It evolved from a static dataset-based application into a robust, full-stack platform that leverages advanced AI to provide dynamic, hyper-personalized outfit generation and seamless virtual try-ons.

Unlike traditional catalog browsers, Vestiary acts as an intelligent personal stylist. It considers multidimensional user preferences—ranging from occasion and weather to body type and color theory—to synthesize complete looks, including accessories and undergarment recommendations.

### Core Capabilities

*   🧠 **Intelligent Styling Engine:** Dynamically generates cohesive outfits based on 6 core data points (gender, body type, preferred color, weather, occasion, style preference).
*   📸 **Virtual Try-On (VTON):** Integrates with the **LightX API** to allow users to virtually try on recommended garments by uploading their own photos. Features a highly robust, multi-step asynchronous integration with intelligent polling mechanisms.
*   🎥 **Cinematic AI Generation:** Visualizes outfit concepts using high-quality, cinematic/Ghibli-style imagery generated via Pollinations AI and curated Unsplash photography.
*   🛍️ **Cross-Platform "Shop the Look":** Instantly provides accurate search links and comparative pricing (USD/INR) across major e-commerce platforms including Amazon, Myntra, Flipkart, Ajio, Zara, and H&M.
*   👙 **Contextual Undergarment Module:** Offers specialized lingerie and undergarment guidance tailored precisely for specific outfits (e.g., advising on plunge bras for wedding gowns or adhesive bras for backless party wear).
*   ✨ **Premium UX/UI:** Built with a modern aesthetic featuring glassmorphism, fluid animations, and a responsive grid layout.

### Tech Stack

#### Client-Side (Frontend)
*   **Framework:** React 19 / Vite
*   **Styling:** Vanilla CSS (Modern Glassmorphism Design System)
*   **Routing:** React Router v7

#### Server-Side (Backend)
*   **Framework:** FastAPI (Python 3.10+)
*   **Server:** Uvicorn (ASGI)
*   **Data Validation:** Pydantic
*   **HTTP Client:** HTTPX (for asynchronous API calls)

#### External Integrations
*   **Virtual Try-On:** LightX API
*   **Image Generation:** Pollinations AI (Prompt-to-Image)
*   **Fashion Imagery:** Unsplash Source

---

## Getting Started

Follow these instructions to set up the project locally for development and testing.

### Prerequisites

Ensure you have the following installed on your local machine:
*   [Node.js](https://nodejs.org/en/) (v18 or higher)
*   [Python](https://www.python.org/downloads/) (v3.9 or higher)
*   Git

### Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SAK-SHI14/Vestiary.git
   cd Vestiary
   ```

2. **Start the Backend Engine (FastAPI)**
   ```bash
   cd backend
   
   # Optional: Create a virtual environment
   # python -m venv venv
   # source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
   
   # Install backend dependencies
   pip install -r requirements.txt
   
   # Run the development server
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   *The backend will be available at: `http://localhost:8000`*
   *Interactive API Documentation (Swagger UI): `http://localhost:8000/docs`*

3. **Start the Frontend Application (React/Vite)**
   Open a new terminal session:
   ```bash
   cd frontend
   
   # Install Node dependencies
   npm install
   
   # Start the Vite development server
   npm run dev
   ```
   *The frontend will be available at the local URL provided by Vite (e.g., `http://localhost:5173`)*

---

## System Architecture

Vestiary utilizes a decoupled client-server architecture, allowing for scalable deployments and independent iteration of the frontend and backend services.

1.  **Client Layer:** The React frontend captures user preferences and image uploads. It handles UI state, animations, and renders data fetched from the API.
2.  **API Gateway (FastAPI):** Acts as the central orchestrator. It receives client requests, runs the styling logic heuristics, generates the appropriate prompts for AI imagery, and structures the response payload.
3.  **VTON Worker (Async):** For virtual try-on requests, the backend initiates an asynchronous job lifecycle with LightX:
    *   Requests a pre-signed S3 upload URL.
    *   Uploads the user's base64 image bytes.
    *   Submits the VTON job combining the user image and target garment URL.
    *   Polls the order status endpoint until the processed image is returned or times out.
4.  **External Distribution:** Product links dynamically route users to external e-commerce platforms via parameterized search queries.

---

## API Reference

The backend provides a comprehensive RESTful API. Below are the core endpoints.

### `POST /generate_outfit`
Generates a complete fashion recommendation based on contextual inputs.

**Request Body:** `application/json`
```json
{
  "gender": "female",
  "body_type": "hourglass",
  "preferred_color": "burgundy",
  "weather": "chilly",
  "occasion": "party",
  "style_preference": "elegant"
}
```

### `POST /try_on`
Initiates a Virtual Try-On asynchronous job.

**Request Body:** `application/json`
```json
{
  "person_image_base64": "data:image/jpeg;base64,/9j/4AAQSkZJ...",
  "garment_url": "https://example.com/dress.jpg",
  "garment_description": "burgundy Sequin Midi Dress"
}
```

---

## Deployment

Vestiary is designed for modern cloud infrastructure:

*   **Frontend (Static Hosting):** Optimized for deployment on Vercel, Netlify, or AWS Amplify. Make sure to set the build directory to `/dist` and the root folder to `/frontend`.
*   **Backend (Containerized / Serverless):** Deployable via Render, Heroku, AWS App Runner, or Docker. Set the startup command to `uvicorn main:app --host 0.0.0.0 --port $PORT`.

---

## Roadmap

- [x] Initial FastAPI & React Migration.
- [x] Integration of External Image Generation (Pollinations AI).
- [x] Cross-Platform E-commerce Link Generation.
- [x] Advanced Virtual Try-On integration via LightX API.
- [ ] Implement user authentication and wardrobe saving mechanisms.
- [ ] Add direct integration with e-commerce APIs (e.g., Amazon PAAPI) for real-time inventory and exact pricing.
- [ ] Introduce a community feed for sharing generated styles.

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Contact

**Sakshi Verma** - Software Engineer & System Architect  
[GitHub Profile](https://github.com/SAK-SHI14)  
Project Link: [https://github.com/SAK-SHI14/Vestiary](https://github.com/SAK-SHI14/Vestiary)

<p align="center">
  <i>Built with passion to redefine digital fashion.</i>
</p>

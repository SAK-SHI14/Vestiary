# Vestiary AI Fashion Stylist ✨

A modern, complete AI-powered fashion recommendation and virtual try-on web application.

## Overview
Vestiary has evolved into a robust full-stack Web Application that merges intelligent fashion styling with advanced AI visual features. It generates unlimited dynamic outfit suggestions, offers smart styling and undergarment advice, provides exact "Shop the Look" links across popular e-commerce platforms, and now features a powerful **Virtual Try-On** engine using the LightX API.

## Tech Stack
* **Frontend:** React.js, Vite, Vanilla CSS with Glassmorphism, Responsive Grid UI
* **Backend:** Python + FastAPI (Production-ready, highly concurrent API endpoints)
* **AI Visual System:** 
  * High-quality cinematic/Ghibli-style product image rendering leveraging curated Unsplash photography and Pollinations AI.
  * Advanced Virtual Try-On (VTON) using the LightX external API.
* **Architecture:** Scalable standard API <-> Client architecture, structured for easy serverless deployment.

## Core Features
1. **Virtual Try-On (VTON) Engine** - Seamlessly upload an image of yourself to try on recommended outfits. Features a robust, multi-step asynchronous integration with the LightX API, complete with intelligent polling and null-safe rendering.
2. **Cinematic AI Outfit Generation** - Recommends unlimited clothing combinations styled dynamically and visualized with premium, highly relevant cinematic imagery.
3. **Smart Recommendation Engine** - Parses multiple dimensions of user preference (gender, body type, preferred color, weather, occasion, style) to serve meticulously optimized looks.
4. **Intelligent Undergarment Module** - Specific, contextual lingerie and undergarment guidance tailored precisely for complex party/wedding apparel and daily wear alike.
5. **Curated Product Search & Price Integration** - Instantly links products across multiple trusted platforms (Amazon, Myntra, Flipkart, Ajio, Zara, H&M). Offers accurate search links and comparative pricing in USD/INR.
6. **Modern UI/UX** - Fluid animations, glass effect cards, responsive layout, distinct product images preventing duplication, and zero 502 Bad Gateway dead links.

## How to Run Locally

### 1. Start the FastAPI Backend
Open your terminal and run the following:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
*The backend API will run on http://localhost:8000*

### 2. Start the React Frontend
In a new terminal window, start the React application:
```bash
cd frontend
npm install
npm run dev
```
*The React UI will run on http://localhost:5173*.

## Deployment Instructions
* **Frontend:** Can be deployed directly to Vercel or Netlify by linking the `frontend` folder to the repository. Ensure build command is `npm run build` and publish directory is `dist`.
* **Backend:** Deploy the `backend` folder via Render, Heroku, or AWS. Set `uvicorn main:app --host 0.0.0.0 --port $PORT` as the start script.

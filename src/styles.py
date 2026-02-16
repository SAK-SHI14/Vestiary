import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Import Font */
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Playfair+Display:wght@700&display=swap');

        /* Global Reset for Text Color */
        html, body, [class*="css"], .stMarkdown, h1, h2, h3, h4, h5, h6, p, label, .stSelectbox label {
            font-family: 'Lato', sans-serif;
            color: #111111 !important; /* Force Black Text */
        }

        /* Headers */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
        }

        /* SideBar */
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            border-right: 1px solid #ddd;
        }
        [data-testid="stSidebar"] * {
            color: #333333 !important;
        }

        /* Main Background */
        .stApp {
            background-color: #ffffff;
            /* Subtle pattern */
            background-image: radial-gradient(#e0e0e0 1px, transparent 1px);
            background-size: 20px 20px;
        }

        /* Cards */
        .outfit-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: transform 0.2s;
        }
        .outfit-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-color: #333;
        }
        
        .outfit-card p {
            margin: 5px 0;
            color: #444 !important;
        }
        
        /* Buttons */
        .stButton button {
            background-color: #000000;
            color: #ffffff !important;
            border-radius: 5px;
            border: none;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #333333;
            color: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    st.title("AI Recommendation App") 
    st.caption("Curated fashion for the modern era.")
    st.markdown("---")

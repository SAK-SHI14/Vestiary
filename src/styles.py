import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Import Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Fauna+One&family=Lato:wght@300;400&display=swap');

        /* Global Vars */
        :root {
            --bg-color: #FDFBF7; /* Very light cream */
            --sidebar-bg: #121212; /* Dark Sidebar to match "black boxes" theme often implies dark mode or contrast */
            --text-primary: #1B1B1B;
            --text-secondary: #555555;
            --accent-color: #D4AF37;
            --card-bg: #FFFFFF;
            --card-details-bg: #000000;
        }

        /* Main Background */
        .stApp {
            background-color: var(--bg-color);
        }

        /* Sidebar - Keeping it dark ensures the "white boxes" pop */
        [data-testid="stSidebar"] {
            background-color: #000000;
            border-right: 1px solid #333;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {
            color: #D4AF37 !important; /* Gold text headers/labels */
        }
        [data-testid="stSidebar"] p {
            color: #FFFFFF !important;
        }
        
        /* Typography */
        html, body, [class*="css"], .stMarkdown, p, label, .stSelectbox label, .stTextInput label {
            font-family: 'Lato', sans-serif;
            color: var(--text-primary);
            line-height: 1.6;
        }

        h1, h2, h3 {
            font-family: 'Lato', sans-serif;
            color: var(--text-primary) !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        h1 {
            font-size: 3.5rem !important;
            font-weight: 400;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        /* Caption centered under title */
        .stCaption {
            font-family: 'Lato', sans-serif;
            color: var(--text-secondary) !important;
            font-size: 1.1rem;
            letter-spacing: 0.1em;
            margin-bottom: 4rem;
            text-align: center;
        }

        /* Cards */
        .outfit-card {
            background-color: var(--card-bg);
            border: 1px solid #F0F0F0;
            padding: 0; 
            margin-bottom: 40px;
            transition: all 0.5s ease;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        
        .outfit-card:hover {
            border-color: #D4AF37;
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }

        .outfit-card img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.8s ease;
        }
        
        .outfit-card:hover img {
            transform: scale(1.03);
        }

        /* BLACK BOX DETAILS */
        .card-details {
            padding: 25px 20px;
            text-align: center;
            background: #000000; /* Black Box */
            position: relative;
            z-index: 2;
        }

        .card-title {
            font-family: 'Lato', sans-serif;
            font-size: 0.95rem;
            color: #D4AF37 !important; /* Gold Text */
            margin-bottom: 8px;
            white-space: nowrap; 
            overflow: hidden;
            text-overflow: ellipsis; 
        }

        .card-subtitle {
            font-family: 'Lato', sans-serif;
            font-size: 0.75rem;
            color: #FFFFFF; /* White Text */
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        /* Buttons - Solid Minimalist */
        .stButton button {
            background-color: #1B1B1B !important;
            color: #D4AF37 !important;
            border: 1px solid #D4AF37 !important;
            border-radius: 0 !important;
            font-family: 'Lato', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 0.2em;
            font-size: 0.7rem;
            padding: 14px 0;
            margin-top: 10px;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton button p {
            color: #D4AF37 !important;
        }
        
        .stButton button:hover {
            background-color: #D4AF37 !important;
            color: #1B1B1B !important;
            border: 1px solid #D4AF37 !important;
        }
        
        /* WHITE BOX SIDEBAR INPUTS */
        /* Selectbox & Input Container */
        .stSelectbox div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div {
            background-color: #FFFFFF !important; /* White Box */
            border: 1px solid #CCC;
            border-radius: 0;
            color: #000000 !important;
        }
        
        /* Dropdown Items */
        div[role="listbox"] li {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
        
        /* Text inside the selectbox/input */
        .stSelectbox div[data-testid="stMarkdownContainer"] p {
            color: #000000 !important; /* Force Black Text */
        }
        .stSelectbox svg {
            fill: #000000 !important; /* Black Arrow */
        }
        
        /* Remove streamline padding */
        .block-container {
            padding-top: 3rem;
            padding-bottom: 5rem;
        }
        
        /* Separator */
        hr {
            margin: 3em 0;
            border-color: #EAE6DE;
        }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    st.title("V E S T I A R Y") 
    st.caption("Curated Fashion Intelligence")
    st.markdown("---")

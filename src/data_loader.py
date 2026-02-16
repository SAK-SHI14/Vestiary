import pandas as pd
import os
import streamlit as st

@st.cache_data
def load_data(csv_path='styles.csv'):
    try:
        df = pd.read_csv(csv_path, on_bad_lines='skip', encoding='utf-8')
    except FileNotFoundError:
        st.error(f"Dataset not found at {csv_path}. Please check the file path.")
        return pd.DataFrame()

    # Normalize columns
    for col in ['gender', 'usage', 'baseColour', 'articleType']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    
    # Image Paths (Handling the nested structure)
    # Assumes images are in 'images/images/' relative to where app.py is run
    df['image_path'] = 'images/images/' + df['id'].astype(str) + '.jpg'
    
    # Derived Columns
    df['color_group'] = df['baseColour'].apply(map_color_group)
    df['weather_compatibility'] = df['articleType'].apply(map_weather)
    
    if 'popularity_score' not in df.columns:
        df['popularity_score'] = 0
        
    return df

def map_color_group(color):
    color = str(color).lower()
    if color in ['red', 'orange', 'yellow', 'maroon', 'gold', 'mustard', 'rust']:
        return 'warm'
    elif color in ['blue', 'green', 'purple', 'cyan', 'teal', 'navy', 'indigo']:
        return 'cool'
    elif color in ['white', 'grey', 'black', 'silver', 'charcoal', 'off white']:
        return 'neutral'
    elif color in ['brown', 'olive', 'beige', 'tan', 'khaki', 'cream']:
        return 'natural'
    elif color in ['pink', 'lime', 'magenta', 'coral', 'neon']:
        return 'bright'
    else:
        return 'other'

def map_weather(article):
    article = str(article).lower()
    if any(word in article for word in ['jacket', 'sweater', 'coat', 'hoodie', 'sweatshirt', 'blazer']):
        return 'cold'
    elif any(word in article for word in ['t-shirt', 'shorts', 'tank', 'dress', 'skirt', 'top', 'camisole']):
        return 'hot'
    elif any(word in article for word in ['rain', 'waterproof', 'umbrella']):
        return 'rainy'
    elif any(word in article for word in ['pants', 'jeans', 'trousers', 'leggings', 'kurta', 'saree']):
        return 'cool' 
    else:
        return 'any'

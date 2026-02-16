import streamlit as st
import os

# Import modules from src
from src.data_loader import load_data
from src.recommender import filter_outfits, get_colour_name
from src.styles import apply_custom_styles, render_header
from src.utils import get_upscaled_image

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Vestiary 🪄",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Premium Styles
apply_custom_styles()

# -----------------------------------------------------------------------------
# Data Loading
# -----------------------------------------------------------------------------
with st.spinner("Loading Fashion Dataset..."):
    df = load_data()

if df.empty:
    st.stop()

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
render_header()

# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("Refine Your Style")
    
    gender = st.selectbox("Gender", ["Female", "Male", "Unisex"]).lower()
    
    usage_list = sorted(list(df['usage'].unique())) if 'usage' in df.columns else ["Casual", "Formal"]
    occasion = st.selectbox("Occasion", [u.capitalize() for u in usage_list]).lower()
    
    weather = st.selectbox("Current Weather", ["Hot", "Cold", "Rainy", "Any"]).lower()
    
    st.markdown("### Color Palette")
    fav_color = st.color_picker("Accent Color", "#D4AF37")
    
    with st.expander("Advanced Filters"):
        color_group_option = st.selectbox("Tone", ["Any", "warm", "cool", "neutral", "bright", "natural"])
        weather_compat = st.selectbox("Weather Compatibility", ["Any", "hot", "cold", "cool", "rainy"])

# -----------------------------------------------------------------------------
# Logic
# -----------------------------------------------------------------------------
color_name = get_colour_name(fav_color).lower()
filtered_df = filter_outfits(df, gender, occasion, color_group_option, weather, weather_compat, color_name)

# -----------------------------------------------------------------------------
# Display
# -----------------------------------------------------------------------------
st.markdown(f"**{len(filtered_df)}** styles found matching your criteria.")

if filtered_df.empty:
    st.warning("No outfits found. Try adjusting the filters.")
else:
    # Grid Layout
    MAX_ITEMS = 40
    results = filtered_df.head(MAX_ITEMS)
    
    cols = st.columns(4) 
    for idx, (i, row) in enumerate(results.iterrows()):
        with cols[idx % 4]:
            image_path = row['image_path']
            
            # Card Container
            with st.container():
                st.markdown('<div class="outfit-card">', unsafe_allow_html=True)
                
                if os.path.exists(image_path):
                    # Upscale functionality remains
                    img_array = get_upscaled_image(image_path)
                    st.image(img_array, use_container_width=True)
                else:
                    st.warning("Image missing")
                
                # Details Section
                st.markdown(f"""
                <div class="card-details">
                    <div class="card-title">{row.get('productDisplayName', 'Luxury Item')}</div>
                    <div class="card-subtitle">{row.get('articleType', 'Accessory')} | {row.get('baseColour', 'Classic')}</div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("VIEW DETAILS", key=f"btn_{row['id']}"):
                    st.toast(f"Added {row['productDisplayName']} to collection.")
                
                st.markdown('</div>', unsafe_allow_html=True)

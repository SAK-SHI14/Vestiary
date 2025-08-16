import os
import random
import streamlit as st
import pandas as pd
from difflib import SequenceMatcher

# --- Page config ---
st.set_page_config(
    page_title="Vestiary",
    page_icon="🪄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    '<meta name="description" content="Vestiary: AI-powered outfit recommendations for every style and occasion.">',
    unsafe_allow_html=True
)

# --- Constants ---
IMAGE_PATH = "images"

# --- Load data ---
@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_csv("styles.csv", on_bad_lines="skip")
    needed_cols = ["id","gender","masterCategory","subCategory","articleType","baseColour","season","usage","productDisplayName"]
    df = df[needed_cols].copy()
    for col in needed_cols[1:]:
        df[col] = df[col].astype(str).str.strip()
    df_norm = df.copy()
    for col in ["gender","baseColour","season","usage"]:
        df_norm[col] = df_norm[col].str.lower()
    return df, df_norm

def get_image_path(product_id):
    for ext in [".jpg", ".jpeg", ".png"]:
        img_path = os.path.join(IMAGE_PATH, str(product_id) + ext)
        if os.path.exists(img_path):
            return img_path
    return None

# --- Mapping helpers ---
def map_gender(user_gender: str):
    g = (user_gender or "").strip().lower()
    if g in ["female","woman","women"]: return ["women"]
    if g in ["male","man","men"]: return ["men"]
    if g in ["boy","boys"]: return ["boys"]
    if g in ["girl","girls"]: return ["girls"]
    if g == "unisex": return ["unisex"]
    return ["women","men","boys","girls","unisex"]

def map_occasion(user_occ: str, df_norm):
    o = (user_occ or "").strip().lower()
    uniques = sorted(x for x in df_norm["usage"].dropna().unique())
    mapping = {
        "casual": ["casual","smart casual"],
        "formal": ["formal"],
        "sports": ["sports"],
        "party": ["party"],
        "ethnic": ["ethnic"],
        "travel": ["travel"],
        "home": ["home"],
        "any": uniques
    }
    return mapping.get(o, uniques)

def map_weather(user_weather: str, df_norm):
    w = (user_weather or "").strip().lower()
    uniques = sorted(x for x in df_norm["season"].dropna().unique())
    mapping = {
        "hot": ["summer"],
        "cold": ["winter"],
        "mild": ["spring","fall"],
        "rainy": ["spring","fall"],
        "any": uniques
    }
    return mapping.get(w, uniques)

def fuzzy_match_ratio(a: str, b: str):
    try:
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()
    except Exception:
        return 0.0

# --- Color helpers ---
BASIC_COLOR_BUCKETS = {
    "black": (0,0,0),
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,128,0),
    "blue": (0,0,255),
    "yellow": (255,255,0),
    "orange": (255,165,0),
    "purple": (128,0,128),
    "pink": (255,192,203),
    "brown": (150,75,0),
    "grey": (128,128,128),
    "navy": (0,0,128)
}

def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) != 6: return None
    try:
        return tuple(int(h[i:i+2], 16) for i in (0,2,4))
    except Exception:
        return None

def closest_basic_color_name_from_hex(hex_color: str):
    rgb = hex_to_rgb(hex_color)
    if rgb is None: return None
    def dist(a,b): return sum((a[i]-b[i])**2 for i in range(3))
    best = min(BASIC_COLOR_BUCKETS.items(), key=lambda kv: dist(rgb, kv[1]))[0]
    return best

# --- Recommendation logic ---
def recommend(df, df_norm, gender="Female", occasion="Casual", weather="Hot", colors=None, top_k=20):
    colors = colors or ["any"]
    genders = map_gender(gender)
    usages = map_occasion(occasion, df_norm)
    seasons = map_weather(weather, df_norm)
    
    filt = df_norm[df_norm["gender"].isin(genders)
                   & df_norm["usage"].isin(usages)
                   & df_norm["season"].isin(seasons)].copy()
    
    if colors != ["any"]:
        filt["color_score"] = filt["baseColour"].apply(
            lambda c: max([fuzzy_match_ratio(c, color) for color in colors])
        )
        filt = filt.sort_values("color_score", ascending=False)
        if filt.empty or filt["color_score"].max() < 0.35:
            filt = df_norm[df_norm["gender"].isin(genders)
                           & df_norm["usage"].isin(usages)].copy()
            filt = filt.sample(min(top_k*2, len(filt)), random_state=42)
            filt["color_score"] = 0.0
    else:
        filt["color_score"] = 0.0
    
    filt = filt.sort_values("color_score", ascending=False)
    out = df.loc[filt.index, ["id","gender","usage","season","baseColour","articleType","productDisplayName"]].head(top_k)
    return out

df, df_norm = load_data()

# --- Sidebar ---
with st.sidebar:
    st.header("Tell us about yourself 🪄")
    gender = st.selectbox("Gender", ["Female","Male","Unisex","Girls","Boys"], index=0)
    occasion = st.selectbox("Occasion", ["Casual","Formal","Party","Sports","Ethnic","Travel","Home","Any"], index=0)
    weather = st.selectbox("Weather", ["Hot","Cold","Mild","Any"], index=0)
    picked_hex = st.color_picker("Pick your favorite color", value="#000000")
    typed_color = st.text_input("...or type a color name (optional)", value="")
    
    effective_colors = [c.strip().lower() for c in typed_color.split(",")] if typed_color else [closest_basic_color_name_from_hex(picked_hex) or "any"]
    topk = st.slider("How many recommendations?", 5, 50, 20, 5)
    st.caption(f"Using color(s): **{', '.join(effective_colors)}** (derived from your input). Set to 'Any' to relax color filter.")

# --- Main page ---
st.title("🪄 Vestiary")
st.write("We match your preferences to fashion data and show the best-fitting outfits!")

with st.expander("Your Preferences", expanded=True):
    st.write(f"- Gender: **{gender}**")
    st.write(f"- Occasion: **{occasion}**")
    st.write(f"- Weather: **{weather}**")
    st.write(f"- Favorite Color(s): **{', '.join(effective_colors)}**")

# --- Get recommendations ---
recs = recommend(df, df_norm, gender=gender, occasion=occasion, weather=weather, colors=effective_colors, top_k=topk)

st.subheader("👗 Recommended Outfits")
if recs.empty:
    st.warning("No matching outfits found. Try relaxing a filter (e.g., set color to Any).")
else:
    for _, row in recs.iterrows():
        with st.container():
            cols = st.columns([1, 2])
            img_path = get_image_path(row['id'])
            with cols[0]:
                if img_path:
                    st.image(img_path, caption=row['productDisplayName'], use_container_width=True)
                else:
                    st.text("❌ No image")
            with cols[1]:
                st.markdown(f"**{row['productDisplayName']}**")
                st.write(f"👤 Gender: {row['gender']}")
                st.write(f"🎯 Occasion: {row['usage']}")
                st.write(f"🌤️ Season: {row['season']}")
                st.write(f"🎨 Color: {row['baseColour']}")
                st.write(f"👕 Article Type: {row['articleType']}")
        st.markdown("---")

    csv = recs.to_csv(index=False).encode("utf-8")
    st.download_button("Download recommendations as CSV", data=csv, file_name="recommendations.csv", mime="text/csv")

st.caption("Note: Body type isn't available in the dataset, so it's not used for filtering.")

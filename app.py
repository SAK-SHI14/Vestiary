import os
import streamlit as st
import pandas as pd
from difflib import SequenceMatcher

st.set_page_config(page_title="AI Outfit Recommendation System", page_icon="👗", layout="wide")

# 👇 set your local image path here
IMAGE_PATH = r"C:\Users\SAKSHI VERMA\OneDrive\Desktop\AI Outfit Recomendation\AI-Outfit-Recomendation-\images"

@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_csv("styles.csv", on_bad_lines="skip")
    # removed 'year' column
    needed_cols = ["id","gender","masterCategory","subCategory","articleType","baseColour","season","usage","productDisplayName"]
    df = df[needed_cols].copy()
    for col in ["gender","masterCategory","subCategory","articleType","baseColour","season","usage","productDisplayName"]:
        df[col] = df[col].astype(str).str.strip()
    df_norm = df.copy()
    for col in ["gender","baseColour","season","usage"]:
        df_norm[col] = df_norm[col].str.lower()
    return df, df_norm

def get_image_path(product_id):
    """Return path to image if it exists, else None"""
    for ext in [".jpg", ".jpeg", ".png"]:  # check common extensions
        img_path = os.path.join(IMAGE_PATH, str(product_id) + ext)
        if os.path.exists(img_path):
            return img_path
    return None

def map_gender(user_gender: str):
    g = (user_gender or "").strip().lower()
    if g in ["female","woman","women"]:
        return ["women"]
    if g in ["male","man","men"]:
        return ["men"]
    if g in ["boy","boys"]:
        return ["boys"]
    if g in ["girl","girls"]:
        return ["girls"]
    if g in ["unisex"]:
        return ["unisex"]
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
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i+2], 16) for i in (0,2,4))
    except Exception:
        return None

def closest_basic_color_name_from_hex(hex_color: str):
    rgb = hex_to_rgb(hex_color)
    if rgb is None:
        return None
    def dist(a,b):
        return sum((a[i]-b[i])**2 for i in range(3))
    best = min(BASIC_COLOR_BUCKETS.items(), key=lambda kv: dist(rgb, kv[1]))[0]
    return best

def recommend(df, df_norm, gender="Female", occasion="Casual", weather="Hot", color_name="black", top_k=20):
    genders = map_gender(gender)
    usages = map_occasion(occasion, df_norm)
    seasons = map_weather(weather, df_norm)
    color = (color_name or "").strip().lower()
    
    filt = df_norm[
        df_norm["gender"].isin(genders)
        & df_norm["usage"].isin(usages)
        & df_norm["season"].isin(seasons)
    ].copy()
    
    if color and color != "any":
        filt["color_score"] = filt["baseColour"].apply(
            lambda c: 1.0 if color in c else fuzzy_match_ratio(color, c)
        )
        filt = filt.sort_values("color_score", ascending=False)
        if not filt.empty and filt["color_score"].max() < 0.35:
            pass
        else:
            filt = filt.head(800)
    else:
        filt["color_score"] = 0.0
    
    if filt.empty:
        filt = df_norm[df_norm["gender"].isin(genders) & df_norm["usage"].isin(usages)].copy()
        filt["color_score"] = filt["baseColour"].apply(lambda c: fuzzy_match_ratio(color, c) if color else 0.0)
    if filt.empty:
        filt = df_norm[df_norm["gender"].isin(genders)].copy()
        filt["color_score"] = filt["baseColour"].apply(lambda c: fuzzy_match_ratio(color, c) if color else 0.0)
    if filt.empty:
        filt = df_norm.copy()
        filt["color_score"] = 0.0
    
    # sort only by color_score (year removed)
    filt = filt.sort_values(["color_score"], ascending=[False])
    
    # no 'year' column anymore
    out = df.loc[filt.index, ["id","gender","usage","season","baseColour","articleType","productDisplayName"]].head(top_k)
    return out

df, df_norm = load_data()

with st.sidebar:
    st.header("Tell us about yourself")
    gender = st.selectbox("Gender", ["Female","Male","Unisex","Girls","Boys"], index=0)
    occasion = st.selectbox("Occasion", ["Casual","Formal","Party","Sports","Ethnic","Travel","Home","Any"], index=0)
    weather = st.selectbox("Weather", ["Hot","Cold","Mild","Any"], index=0)
    picked_hex = st.color_picker("Pick your favorite color", value="#000000")
    typed_color = st.text_input("...or type a color name (optional)", value="black")
    effective_color = typed_color.strip() or (closest_basic_color_name_from_hex(picked_hex) or "any")
    topk = st.slider("How many recommendations?", 5, 50, 20, 5)
    st.caption(f"Using color: **{effective_color}** (derived from your input). Set to 'Any' to relax color filter.")

st.title("👗 AI Outfit Recommendation System")
st.write("We match your preferences to Myntra-style data and show the best-fitting items.")

with st.expander("Your Preferences", expanded=True):
    st.write(f"- Gender: **{gender}**")
    st.write(f"- Occasion: **{occasion}**")
    st.write(f"- Weather: **{weather}**")
    st.write(f"- Favorite Color: **{effective_color}**")

recs = recommend(df, df_norm, gender=gender, occasion=occasion, weather=weather, color_name=effective_color, top_k=topk)

st.subheader("👕 Recommended Outfits")
if recs.empty:
    st.warning("No matching outfits found. Try relaxing a filter (e.g., set color to Any).")
else:
    for _, row in recs.iterrows():
        img_path = get_image_path(row['id'])
        col1, col2 = st.columns([1, 3])
        with col1:
            if img_path:
                st.image(img_path, caption=row['productDisplayName'], width=180)
            else:
                st.text("❌ No image")
        with col2:
            st.markdown(f"**{row['productDisplayName']}**")
            st.write(f"👤 Gender: {row['gender']}")
            st.write(f"🎯 Occasion: {row['usage']}")
            st.write(f"🌤️ Season: {row['season']}")
            st.write(f"🎨 Color: {row['baseColour']}")
            st.write(f"👕 Article Type: {row['articleType']}")

    csv = recs.to_csv(index=False).encode("utf-8")
    st.download_button("Download recommendations as CSV", data=csv, file_name="recommendations.csv", mime="text/csv")

st.caption("Note: Body type isn't available in the dataset, so it's not used for filtering.")

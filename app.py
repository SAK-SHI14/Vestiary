import streamlit as st
import pandas as pd
import os
import webcolors
from difflib import get_close_matches

# Load dataset
df = pd.read_csv('styles.csv', on_bad_lines='skip', encoding='utf-8')

# Normalize dataset columns
for col in ['gender', 'usage', 'baseColour', 'articleType']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.lower().str.strip()
    else:
        st.error(f"Column '{col}' missing in dataset!")
        st.stop()

# Prepare image paths
df['image_path'] = 'images/' + df['id'].astype(str) + '.jpg'

# Derived Columns
def map_color_group(color):
    color = str(color).lower()
    if color in ['red', 'orange', 'yellow', 'maroon']:
        return 'warm'
    elif color in ['blue', 'green', 'purple', 'cyan']:
        return 'cool'
    elif color in ['white', 'grey', 'black']:
        return 'neutral'
    elif color in ['brown', 'olive', 'beige']:
        return 'natural'
    elif color in ['pink', 'lime', 'teal']:
        return 'bright'
    else:
        return 'unknown'

def map_weather(article):
    article = str(article).lower()
    if any(word in article for word in ['jacket', 'sweater', 'coat', 'hoodie']):
        return 'cold'
    elif any(word in article for word in ['t-shirt', 'shorts', 'tank']):
        return 'hot'
    elif any(word in article for word in ['rain', 'waterproof']):
        return 'rainy'
    else:
        return 'cool'

df['color_group'] = df['baseColour'].apply(map_color_group)
df['weather_compatibility'] = df['articleType'].apply(map_weather)
df['popularity_score'] = 0

# Streamlit UI
st.title("👗 AI Outfit Recommendation System")

# Sidebar Inputs
st.sidebar.header("Tell us about yourself")
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Other"]).lower()
body_type = st.sidebar.selectbox("Body Type", ["Slim", "Average", "Curvy", "Athletic"]).lower()
occasion = st.sidebar.selectbox("Occasion", ["Casual", "Formal", "Party", "Workout"]).lower()
weather = st.sidebar.selectbox("Weather", ["Hot", "Cold", "Rainy"]).lower()
fav_color = st.sidebar.color_picker("Pick your favorite color")

color_group_option = st.sidebar.selectbox("Color Group (Mood of Color)", ["Any", "warm", "cool", "neutral", "natural", "bright"])
weather_option = st.sidebar.selectbox("Weather Compatibility", ["Any", "hot", "cold", "cool", "rainy"])

# Updated color functions using fallback
def closest_colour(requested_colour):
    try:
        color_dict = webcolors.CSS3_NAMES_TO_HEX
    except AttributeError:
        color_dict = {
            'white': '#ffffff', 'black': '#000000', 'red': '#ff0000', 'blue': '#0000ff', 'green': '#008000'
        }  # fallback if CSS3 not found

    min_colours = {}
    for name, hex_code in color_dict.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(hex_code)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(hex_code):
    try:
        return webcolors.hex_to_name(hex_code)
    except ValueError:
        r, g, b = webcolors.hex_to_rgb(hex_code)
        return closest_colour((r, g, b))

# Get closest color name
color_name = get_colour_name(fav_color).lower()

# Show selected preferences
st.subheader("🧾 Your Preferences")
st.markdown(f"- Gender: **{gender.capitalize()}**")
st.markdown(f"- Body Type: **{body_type.capitalize()}**")
st.markdown(f"- Occasion: **{occasion.capitalize()}**")
st.markdown(f"- Weather: **{weather.capitalize()}**")
st.markdown(f"- Favorite Color (Hex): **{fav_color}**")
st.markdown(f"- Closest Color Name: **{color_name}**")

# Filtering Logic
filtered_df = df.copy()

# Filter gender
if gender != "other":
    filtered_df = filtered_df[filtered_df['gender'].str.contains(gender, na=False)]

# Filter by occasion
filtered_df = filtered_df[filtered_df['usage'].str.contains(occasion, na=False)]

# Filter by color name match (relaxed)
color_matches = get_close_matches(color_name, df['baseColour'].unique(), n=1, cutoff=0.3)
if color_matches:
    filtered_df = filtered_df[filtered_df['baseColour'].str.contains(color_matches[0], na=False)]

# Filter by color group
if color_group_option != "Any":
    filtered_df = filtered_df[filtered_df['color_group'] == color_group_option]

# Filter by weather
if weather_option != "Any":
    filtered_df = filtered_df[filtered_df['weather_compatibility'] == weather_option]

# Debug row counts (optional)
# st.write("After filters, rows:", len(filtered_df))

# Output
st.write(f"🎯 Total matching outfits: {len(filtered_df)}")

# Display outfits
st.subheader("👕 Recommended Outfits")
if filtered_df.empty:
    st.warning("No matching outfits found. Try adjusting the filters.")
else:
    for _, row in filtered_df.head(10).iterrows():
        if os.path.exists(row['image_path']):
            st.image(row['image_path'], caption=row.get('productDisplayName', 'No name'), width=250)
            if st.button(f"❤️ Like this - ID {row['id']}", key=row['id']):
                df.loc[df['id'] == row['id'], 'popularity_score'] += 1
                df.to_csv('styles_enhanced.csv', index=False)
                st.success("Thanks for liking! 💖")
        else:
            st.markdown(f"🖼️ Image not found for ID {row['id']}")

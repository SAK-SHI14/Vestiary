import pandas as pd
from difflib import get_close_matches
import webcolors

def filter_outfits(df, gender, occasion, color_group_option, weather, weather_compat, color_name):
    filtered_df = df.copy()

    # Filter gender
    if gender != "unisex": 
        if gender == 'female':
            filtered_df = filtered_df[filtered_df['gender'].isin(['women', 'girls', 'unisex'])]
        elif gender == 'male':
            filtered_df = filtered_df[filtered_df['gender'].isin(['men', 'boys', 'unisex'])]

    # Filter by occasion
    if occasion:
        filtered_df = filtered_df[filtered_df['usage'].str.contains(occasion, na=False, case=False)]

    # Filter by color group
    if color_group_option != "Any":
        filtered_df = filtered_df[filtered_df['color_group'] == color_group_option]

    # Filter by weather
    weather_map = {'hot': 'hot', 'cold': 'cold', 'rainy': 'rainy'}
    if weather in weather_map:
        target = weather_map[weather]
        filtered_df = filtered_df[filtered_df['weather_compatibility'].isin([target, 'any', 'cool'])]
        
    if weather_compat != "Any":
        filtered_df = filtered_df[filtered_df['weather_compatibility'] == weather_compat]

    return filtered_df

# Helper for color matching
def closest_colour(requested_colour):
    try:
        color_dict = webcolors.CSS3_NAMES_TO_HEX
    except AttributeError:
        color_dict = {
            'white': '#ffffff', 'black': '#000000', 'red': '#ff0000', 
            'blue': '#0000ff', 'green': '#008000', 'yellow': '#ffff00'
        }

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

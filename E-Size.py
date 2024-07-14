import streamlit as st
from PIL import Image
import base64

# Function to calculate bra size
def calculate_bra_size(band_measurement, bust_measurement):
    band_size = round(band_measurement)
    bust_size = round(bust_measurement)
    cup_size = bust_size - band_size

    # Map the cup size difference to actual cup sizes
    cup_size_mapping = {
        0: "AA", 1: "A", 2: "B", 3: "C", 4: "D", 5: "DD/E", 6: "DDD/F",
        7: "G", 8: "H", 9: "I", 10: "J", 11: "K"
    }

    cup_letter = cup_size_mapping.get(cup_size, "L or larger")
    return band_size, cup_letter

# Function to suggest dress size
def suggest_dress_size(bust_measurement, waist_measurement, hip_measurement):
    if bust_measurement < 32 and waist_measurement < 25 and hip_measurement < 35:
        return "XS"
    elif 32 <= bust_measurement < 34 and 25 <= waist_measurement < 27 and 35 <= hip_measurement < 37:
        return "S"
    elif 34 <= bust_measurement < 36 and 27 <= waist_measurement < 29 and 37 <= hip_measurement < 39:
        return "M"
    elif 36 <= bust_measurement < 38 and 29 <= waist_measurement < 31 and 39 <= hip_measurement < 41:
        return "L"
    elif 38 <= bust_measurement < 40 and 31 <= waist_measurement < 33 and 41 <= hip_measurement < 43:
        return "XL"
    else:
        return "XXL"

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        .stApp::before {{
            content: '';
            display: block;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.4);
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add local background image with 50% opacity
add_bg_from_local("bra_size_image.jpg")

# Custom CSS for styling
st.markdown(f"""
<style>
.main {{
    background-color: hsla(0, 100%, 70%, 0.3); 
    padding: 20px;
    border-radius: 50px;
    max-width: 1000px;
    margin: 0 auto;
    color: black;
}}
h1 {{
    color: #000000;
}}
.stButton>button {{
    background-color: #ff69b4;
    color: white;
    font-size: 16px;
    border-radius: 5px;
    border: none;
    padding: 10px 20px;
}}
.stButton>button:hover {{
    background-color: #ff1493;
}}
/* Style for specific text elements */
.text-black {{
    color: black !important; /* Ensure text color is black */
}}
.highlight {{
    background-color: #e89aed;
    color: white;
    font-size: 20px;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
}}
</style>
""", unsafe_allow_html=True)

# Streamlit app
#st.title("E-Size: Your Ultimate Dress Size Calculator")

st.header("Calculate bra size.")

band_measurement = st.number_input("Band Measurement (in inches)", min_value=20.0, max_value=50.0, step=0.5)
bust_measurement = st.number_input("Bust Measurement (in inches)", min_value=20.0, max_value=60.0, step=0.5)

if st.button("Calculate "):
    if band_measurement and bust_measurement:
        if bust_measurement <= band_measurement:
            st.error("Bust measurement must be greater than band measurement.")
        else:
            band_size, cup_letter = calculate_bra_size(band_measurement, bust_measurement)
            st.markdown(f'<div class="highlight">Your bra size is: {band_size}{cup_letter}</div>', unsafe_allow_html=True)

st.header("Dress size suggestion")

bust_measurement_dress = st.number_input("Bust Measurement for Dress (in inches)", min_value=20.0, max_value=60.0, step=0.5)
waist_measurement = st.number_input("Waist Measurement (in inches)", min_value=20.0, max_value=50.0, step=0.5)
hip_measurement = st.number_input("Hip Measurement (in inches)", min_value=20.0, max_value=60.0, step=0.5)

if st.button("Calculate Dress Size"):
    if bust_measurement_dress and waist_measurement and hip_measurement:
        dress_size = suggest_dress_size(bust_measurement_dress, waist_measurement, hip_measurement)
        st.markdown(f'<div class="highlight">Suggested dress size: {dress_size}</div>', unsafe_allow_html=True)
    else:
        st.error("Please enter bust, waist, and hip measurements for dress size suggestion.")

st.write("Note: The size may vary slightly depending on the brand.")

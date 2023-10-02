import streamlit as st
import pandas as pd
from PIL import Image
import os
import matplotlib.pyplot as plt

# Path to the directory containing your PNG images
image_folder = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images1"
images = os.listdir(image_folder)
images.sort()  # Ensure images are in the correct order

# Title
st.title("Dashboard - Precipitation and Images")

# Images section with time slider
st.header("Images with Time Slider")

selected_index_images = st.slider("Select Image", 0, len(images) - 1, 0)
image = Image.open(os.path.join(image_folder, images[selected_index_images]))
st.image(image, caption=f"Image {selected_index_images}", use_column_width=True)

# Chart section for the selected city
st.header("Chart - Precipitation")
st.write("Select a city:")

# Dropdown list of cities
cities = ["City 1", "City 2", "City 3"]  # Add more cities as needed
selected_city = st.selectbox("Select City", cities)

# Load CSV data for the selected city
csv_file_path = f"C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv1/{selected_city.lower().replace(' ', '_')}.csv"
csv_data = pd.read_csv(csv_file_path)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(csv_data['Date'], csv_data['Precipitation'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Precipitation")
ax.set_title(f"Precipitation Data for {selected_city}")
st.pyplot(fig)

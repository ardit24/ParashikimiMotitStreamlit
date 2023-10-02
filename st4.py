import streamlit as st
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the directory containing your PNG images
image_folder = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images1"
images = os.listdir(image_folder)
images.sort()  # Ensure images are in the correct order

# Title
st.title("Dashboard - Precipitation and Images")

# Initialize the selected image index
selected_index_images = 0

# Images section with arrow buttons
st.header("Images with Navigation")

# Navigation buttons with arrows
col1, col2, col3, col4, col5 = st.columns(5)
if col2.button("←", key="prev_image", disabled=selected_index_images == 0):
    selected_index_images -= 1
if col4.button("→", key="next_image", disabled=selected_index_images == len(images) - 1):
    selected_index_images += 1

# Display the selected image
image = Image.open(os.path.join(image_folder, images[selected_index_images]))
st.image(image, caption=f"Image {selected_index_images}", use_column_width=True)

# Chart section for the selected city
st.header("Chart - Precipitation")
st.write("Select a city:")

# Dropdown list of cities
cities = ["City 1", "City 2", "City 3"]  # Add more cities as needed
selected_city = st.selectbox("Select City", cities)

# Load CSV data for the selected city
csv_file_path = f"C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv2/{selected_city.lower().replace(' ', '_')}.csv"
csv_data = pd.read_csv(csv_file_path)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(csv_data['Date'], csv_data['Precipitation'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Precipitation")
ax.set_title(f"Precipitation Data for {selected_city}")
st.pyplot(fig)

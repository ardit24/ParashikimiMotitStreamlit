import streamlit as st
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the directory containing your PNG images
image_folder = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images1"
images = os.listdir(image_folder)
images.sort()  # Ensure images are in the correct order

# Load CSV data for the chart
csv_file_path = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv2.csv"
csv_data = pd.read_csv(csv_file_path)

# Title
st.title("Streamlit Dashboard")

# Images section with time slider
st.header("Images with Time Slider")

selected_index_images = st.slider("Select Image", 0, len(images) - 1, 0)
image = Image.open(os.path.join(image_folder, images[selected_index_images]))
st.image(image, caption=f"Image {selected_index_images}", use_column_width=True)

# Chart section
st.header("Chart - Precipitation")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(csv_data['Date'], csv_data['Precipitation'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Precipitation")
ax.set_title("Precipitation Data")
st.pyplot(fig)

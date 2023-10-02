import streamlit as st
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the directory containing your PNG images
image_folder = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images1"
images = os.listdir(image_folder)
images.sort()  # Ensure images are in the correct order

# Sidebar slider for image selection
selected_index_images = st.sidebar.slider("Select Image", 0, len(images) - 1, 0)

# Display the selected image in the upper part
st.image(Image.open(os.path.join(image_folder, images[selected_index_images])),
         caption=f"Image {selected_index_images}",
         use_column_width=True)

# Load CSV data for the chart
csv_file_path = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv1.csv"
csv_data = pd.read_csv(csv_file_path)

# Chart section in the lower part
st.header("Chart - Precipitation")
st.write("Select a data point range:")
start_index = st.slider("Start Index", 0, len(csv_data) - 1, 0)
end_index = st.slider("End Index", start_index, len(csv_data) - 1, len(csv_data) - 1)

# Filter data based on the selected index range
filtered_data = csv_data.iloc[start_index:end_index + 1]

# Create a chart
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Precipitation'], marker='o')
plt.xlabel("Date")
plt.ylabel("Precipitation")
plt.title("Precipitation Data")
st.pyplot(plt)

# You can add more content here as needed

import streamlit as st
from PIL import Image
import os

# Path to the directories containing your PNG images for each page
image_folder_page1 = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images1"
image_folder_page2 = "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images2"

# Sidebar page selection
page = st.sidebar.radio("Select Page", ["Reshjet", "Temperaturat"])

if page == "Reshjet":
    # Reshjet content
    st.title("Reshjet")
    images_page1 = os.listdir(image_folder_page1)
    images_page1.sort()
    selected_index = st.slider("Select Image", 0, len(images_page1) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page1, images_page1[selected_index])), caption=f"Image {selected_index}", use_column_width=True)
else:
    # Temperaturat content
    st.title("Temperaturat")
    images_page2 = os.listdir(image_folder_page2)
    images_page2.sort()
    selected_index = st.slider("Select Image", 0, len(images_page2) - 1, 0)
    st.image(Image.open(os.path.join(image_folder_page2, images_page2[selected_index])), caption=f"Image {selected_index}", use_column_width=True)

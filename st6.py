import streamlit as st
import pandas as pd
from PIL import Image
import os
import altair as alt
import plost as pt

st.sidebar.markdown("<h1 style='font-size: 24px; font-weight: bold;'>PANELI KRYESOR</h1>", unsafe_allow_html=True)
st.sidebar.subheader('Zgjidhni parametrat:')
time_hist_color = st.sidebar.selectbox('Select', ('Date', 'Precipitation')) 

# st.sidebar.subheader('Donut chart parameter')
# donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Zgjidhni parametrat e tabeles:')
plot_data = st.sidebar.multiselect('Select', ['Date', 'Precipitation'], ['Date', 'Precipitation'])

# Define folder paths for images and CSVs for each page
page_data = {
    "Reshjet": {
        "image_folder": "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images1",
        "csv_folder": "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv1"
    },
    "Temperaturat": {
        "image_folder": "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images2",
        "csv_folder": "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv2"
    },
    "Zjarret": {
        "image_folder": "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\images3",
        "csv_folder": "C:\\Users\\35569\\Documents\\Developments\\Forecast-Weather\\csv3"
    }
}


# Sidebar with radio buttons for selecting pages
selected_page = st.sidebar.radio("Select Page", list(page_data.keys()))
url1 = "https://www.facebook.com/InstitutiGjeoshkencave/"
url2 = "https://www.geo.edu.al/Rreth_nesh/IGJEO/"
st.sidebar.markdown("Na ndiqni në [**Faqen zyrtare**](%s) dhe [**Facebook**](%s)" % (url2, url1))
st.sidebar.markdown('''---Designed by Institute of GeoSciences, Tiranë''')


agree = st.checkbox("Klikoni për të lënë feedback-un tuaj")
if agree:
    st.write("Falemindert për kohën tuaj!")


# Page content based on selected page
st.title(f"{selected_page} - Paneli Kryesor")

# Load and display image based on selected page
image_folder = page_data[selected_page]["image_folder"]
images = os.listdir(image_folder)
images.sort()
selected_index_images = st.slider("Kolazhi me foto:", 0, len(images) - 1, 0)
image = Image.open(os.path.join(image_folder, images[selected_index_images]))
st.image(image, caption=f"Image {selected_index_images}", use_column_width=True)

# Add a description below the image
image_description = {
    "Reshjet": "Description for Image on Reshjet.",
    "Temperaturat": "Description for Image on Temperaturat.", 
    "Zjarret": "Description for Image on Zjarret."
}
st.write(image_description[selected_page])

# Chart section for the selected city
st.header(f"Chart - Precipitation ({selected_page})")
st.write("Select a city:")

# Dropdown list of cities
cities = ["City 1", "City 2", "City 3", 'Burrel', 'Belsh', 'Berat', 'Cërrik', 'Devoll', 'Dibër', 'Divjakë', 'Dropull', 'Elbasan', 'Fier', 'Finiq', 'Fushë-Arrëz', 'Gjirokastër', 'Gramsh', 'Has', 'Himarë', 'Kamëz', 'Kavajë', 'Këlcyrë', 'Klos', 'Kolonjë', 'Konispol', 'Korçë', 'Krujë', 'Kuçovë', 'Kukës', 'Kurbin', 'Lezhë', 'Libohovë', 'Librazhd', 'Lushnjë', 'Malësi e Madhe', 'Maliq', 'Mallakastër', 'Mat', 'Memaliaj', 'Mirditë', 'Patos', 'Peqin', 'Përmet', 'Pogradec', 'Poliçan', 'Prrenjas', 'Pustec', 'Roskovec', 'Rrogozhinë', 'Sarandë', 'Selenicë', 'Shijak', 'Shkodër', 'Skrapar', 'Tepelenë', 'Tropojë', 'Ura Vajgurore', 'Bulqize', 'Tiranë', 'Durrës', 'Vau i Dejës', 'Vlorë', 'Vorë']  # Add more cities as needed
selected_city = st.selectbox("Select City", cities)

# Load CSV data for the selected city and page // Duhet kontrolluar data !!!
csv_folder = page_data[selected_page]["csv_folder"]
csv_file_path = os.path.join(csv_folder, f"{selected_city.lower().replace(' ', '_')}.csv")
csv_data = pd.read_csv(csv_file_path, parse_dates=['Date'], dayfirst=True)
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')



# Create a bar chart using Altair
thresholds = [10, 20, 30]  # Add your threshold values here

# color_condition = alt.condition(
#     alt.datum.Precipitation > thresholds[-1], alt.value('red'),
#     alt.condition(alt.datum.Precipitation > thresholds[-2], alt.value('yellow'), alt.value('green'))
# )

chart = alt.Chart(csv_data).mark_bar().encode(
    x=alt.X('Date:T', title='Date'),
    y=alt.Y('Precipitation:Q', title='Precipitation'),
    # color=color_condition,
    tooltip=[alt.Tooltip('Date:T', title='Date'), alt.Tooltip('Precipitation:Q', title='Precipitation')]
).properties(
    width=800,  # Increase chart width
    height=400,
    title=f"Precipitation Data for {selected_city}"
).configure_axis(
    labelFontSize=12,  # Increase font size of axis labels
    titleFontSize=14  # Increase font size of axis titles
).configure_mark(
    opacity=0.7  # Adjust bar opacity
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)

# Add legend for the color scale
st.markdown("**Legend:**")
st.markdown("<font color='red'>Red: **Above Highest Threshold**</font> <font color='black'>Yellow: **Above Middle Threshold**</font> <font color='green'>Green: **Below Middle Threshold**</font>", unsafe_allow_html=True)    # Red: Above Highest Threshold
   # Yellow: Above Middle Threshold
   # Green: Below Middle Threshold

# Add a description below the chart
chart_description = {
    "Reshjet": "Description for Chart on Reshjet.",
    "Temperaturat": "Description for Chart on Temperaturat.",
    "Zjarret": "Description for Image on Zjarret."
}
st.write(chart_description[selected_page])

# Add a custom footer aligned to the right side of the sidebar
st.sidebar.markdown(
    "<p style='text-align: right;'>Made with Streamlit by Alban Doko a.doko@igeo.edu.al</p>",
    unsafe_allow_html=True
)

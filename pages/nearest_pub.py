import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Load the pub dataset
df = pd.read_csv('pub.csv')

# Set the page layout to centered
st.set_page_config(layout="centered")

st.markdown("<h1 style='text-align: center; color: #000000; font-weight: bold;'> Find the nearest pub 🍻</h1>", unsafe_allow_html=True)

# Add an image
st.image('pubs2.jpg', use_column_width=True)

# Allow user to enter their latitude and longitude
lat = float(st.number_input("Enter your latitude:", value=51.5074))
lon = float(st.number_input("Enter your longitude:", value=-0.1278))

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

# Calculate the distance between the user's location and each pub in the dataset
df['distance'] = df.apply(lambda row: euclidean_distance(row['latitude'], row['longitude'], lat, lon), axis=1)

# Sort the dataset by distance and display the nearest 5 pubs
nearest_pubs = df.sort_values(by='distance').head(5)
st.write(f"Displaying the 5 nearest pubs to your location (lat: {lat}, lon: {lon}):")
st.dataframe(nearest_pubs)

# Create a map centered on the user's location
m = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker for the user's location
folium.Marker(location=[lat, lon], icon=folium.Icon(color='red'), popup='Your Location').add_to(m)

# Add markers for each of the nearest pubs
marker_cluster = MarkerCluster().add_to(m)
for index, row in nearest_pubs.iterrows():
    Marker([row['latitude'], row['longitude']], popup=row['name']).add_to(marker_cluster)

# Display the map
st.write("Map of the nearest pubs:")
folium_static(m)

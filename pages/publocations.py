import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static


# Load the pub dataset
df = pd.read_csv('pub.csv')

# Set the page layout to centered
st.set_page_config(layout="centered")

st.markdown("<h1 style='text-align: center; color: #000000; font-weight: bold;'>  Pub Locations 🍻</h1>", unsafe_allow_html=True)

# Add an image of a pub
st.image('pubs_uk.jpg', use_column_width=True)

# Allow user to choose between searching by postal code or local authority
search_type = st.radio("Search by:", ('Postal Code', 'Local Authority'))

# Create a list of unique postal codes or local authorities to display in the dropdown menu
if search_type == 'Postal Code':
    search_list = sorted(df['postcode'].unique())
else:
    search_list = sorted(df['local_authority'].unique())

# Allow user to select a postal code or local authority from the dropdown menu
search_value = st.selectbox(f"Select a {search_type}:", search_list)

# Filter the dataset based on the selected postal code or local authority
if search_type == 'Postal Code':
    filtered_data = df[df['postcode'] == search_value]
else:
    filtered_data = df[df['local_authority'] == search_value]

# Display the filtered dataset
st.write(f"Displaying {len(filtered_data)} pubs in {search_value}:")
st.dataframe(filtered_data)

# Create a map centered on the chosen location
m = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=13)

# Add markers for each pub in the filtered dataset
for index, row in filtered_data.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(m)

# Display the map
folium_static(m)

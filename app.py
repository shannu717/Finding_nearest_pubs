import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('pub.csv')

#Setting page layout
st.set_page_config(layout="centered")

st.markdown("<h1 style='text-align: center; color: #b56a67; font-weight: bold;'> Open Pubs Application 🍻</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #000000;'>Welcome to pub finder app! 🎉</h2>", unsafe_allow_html=True) 

# Add an image of a pub
st.image('pubs.jpg', use_column_width=True)

# Display some basic information about the dataset
st.write(f"The dataset contains **{len(df)}** pub locations.")
st.write(f"The dataset covers **{len(df['local_authority'].unique())}** local authorities.") 

st.write("Some statistics about the dataset:")
# st.write(pub_data.describe())
stats = df.describe().T
stats['count'] = stats['count'].astype(int)
stats = stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
st.dataframe(stats.style.highlight_max(axis=0, color='#EB6864'))

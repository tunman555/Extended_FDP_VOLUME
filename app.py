import streamlit as st
import json
from fdp_utils import *
from pathlib import Path

st.title("FDP Volume App. 🗺")
st.markdown("""
    **Introduction:** This interactive dashboard is designed for visualization FDP Volume Definition datasets.
    Several open-source packages are used to process the data and generate the visualization""")

sector_list = list(sector_json.keys())

row1_col1, row1_col2, row1_col3,row1_col4 = st.columns(4)

with row1_col1:
    selected_sector = st.selectbox("Sector", sector_list)
    selected_volume = sector_json[selected_sector]['volume']
    

with row1_col2:
    if selected_sector :
        volume = st.selectbox("Volume",selected_volume)

with row1_col3 :
    show_sector = st.checkbox('Show Sector')

    if show_sector:
        fig = create_sector_plot(selected_sector)
        
with row1_col4 :
    show_3d = st.checkbox('Show 3D')
    if show_3d:
        fig2 = create_3d_plot(volume,selected_sector)

row2_col1,row2_col2 = st.columns([6,1])
with row2_col1:
    if show_sector:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    else:
        fig = create_volume_plot(volume)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with row2_col2:
    if not show_sector :
        selected_layer = fdp_volume[volume]['level']
        box = get_box(selected_layer)
        st.write(f"**Volume:** {volume}")
        st.write(f"**Sector:** {selected_sector}")
        #st.write(f"**Responsibility:** ")
        st.write(f"**Layer:** \n {box[0]} - {box[1]} Ft." )

row3_col1 = st.columns(1)
if show_3d:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
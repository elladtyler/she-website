import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Energy Cost Calculator')
    st.write("Please enter some information about your home, and we'll calculate your energy costs!")

    floor_area =  st.number_input('Total floor area')
    number_floors = st.selectbox('Number of floors', [1, 2, 3])
    climate_zone = st.selectbox('Climate zone', [1, 2, 3])

    space_heater = st.multiselect('Space Heater', [1, 2, 3])
    water_heater = st.multiselect('Water Heater', [1, 2, 3])

    utility = st.selectbox('Utility Company', ['PG&E', 'TID', 'SCE', "Other"])

    rate_schedule = st.selectbox('Rate Schedule', [1, 2, 3])

    #st.select_slider('Slide to select', options=[1, '2'])
    if st.button('Calculate!'):
        st.write("Your results are below:")

        st.write("Floor Area:", floor_area)
        st.write("Number of floors:", number_floors)










    #
    # st.button('Hit me')
    # st.checkbox('Check me out')
    # st.radio('Radio', [1, 2, 3])
    # st.selectbox('Select', [1, 2, 3])
    # st.multiselect('Multiselect', [1, 2, 3])
    # st.slider('Slide me', min_value=0, max_value=10)
    # st.select_slider('Slide to select', options=[1, '2'])
    # st.text_input('Enter some text')
    #
    # st.text_area('Area for textual entry')
    # st.date_input('Date input')
    # st.time_input('Time entry')
    # st.file_uploader('File uploader')
    # st.color_picker('Pick a color')

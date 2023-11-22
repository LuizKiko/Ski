import streamlit as st
from data_access import dfSki, dfSnow, dfCountryCode
from ski import Ski
import time

st.set_page_config(page_title="Data Analysis", page_icon=":bar_chart:", layout="wide")

progressBar = st.progress(0)
for i in range (100):
    time.sleep(0.01)
    progressBar.progress(i+1)

st.sidebar.header("Welcome!")
st.sidebar.markdown("___")

dashboard = st.sidebar.radio(
    "Choose the dashboard:",
    ["Airbnb","USA Flights","Shark Attacks", "Ski Stations"],
    index=3
)
if dashboard == "Ski Stations":
   Ski(dfSki, dfCountryCode, dfSnow)
else:
    st.write("Boards to be added in the future! Stay tunned")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
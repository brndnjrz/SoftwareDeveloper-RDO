import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Team Insights Dashboard", 
    page_icon="💻", 
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items=None)

st.title("Team Insights Dashboard")

st.sidebar.header("Team Update")

name = st.sidebar.text_input("Name")
mood = st.sidebar.slider(
    "Mood (1 = Low, 10 = High)", 
    min_value=1,
    max_value=10, 
    value=5)
update_text = st.sidebar.text_area("What are you working on?")
blockers = st.sidebar.text_area("Any blockers?")

st.sidebar.button("Submit Update")
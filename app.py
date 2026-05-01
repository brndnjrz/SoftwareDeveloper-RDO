import streamlit as st
import pandas as pd
from utils.data_handler import load_data, save_data
from components.team_update_form import render_team_update_form

st.set_page_config(
    page_title="Team Insights Dashboard", 
    page_icon="💻", 
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items=None)

st.title("Team Insights Dashboard")

form_data = render_team_update_form()

if form_data:
    current_data = load_data()
    current_data.append(form_data)
    save_data(current_data)
    st.sidebar.success("Update submitted successfully")

data = load_data()
df = pd.DataFrame(data)

st.subheader("Team Updates")

if df.empty:
    st.info("No updates yet")
else:
    st.dataframe(df, use_container_width=True)

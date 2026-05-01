import streamlit as st
import pandas as pd
from utils.data_handler import load_data, save_data
from components.team_update_form import render_team_update_form

st.set_page_config(
    page_title="Team Insights Dashboard", 
    page_icon="💻", 
    layout="wide", 
    initial_sidebar_state="expanded"
    )

st.title("Team Insights Dashboard")

form_data = render_team_update_form()

if form_data:
    current_data = load_data()
    current_data.append(form_data)
    save_data(current_data)
    st.sidebar.success("Update submitted successfully")

data = load_data()

if data:
    df = pd.DataFrame(data)

    if "timestamp" in df.columns:
        df = df.drop(columns=["timestamp"])

    if "timestamp_display" in df.columns:
        df = df.rename(columns={"timestamp_display": "Submitted At"})

    df.columns = df.columns.str.title()

    st.dataframe(df, use_container_width=True)

else:
    st.info("No updates yet — be the first to check in!")
import streamlit as st
from datetime import datetime


def render_team_update_form() -> dict | None:
    """
    Renders the team check-in form inside the Streamlit sidebar.

    Collects:
        - name       (str)
        - mood       (int, 1–10)
        - update     (str)
        - blockers   (str)
        - timestamp  (str, ISO 8601)

    Returns:
        dict | None: Structured form data on submission, or None if the form has not been submitted yet.
    """

    with st.sidebar:
        st.header("Team Update")

        with st.form(key="team_update_form", clear_on_submit=True):

            name = st.text_input(
                label="Name",
                placeholder="e.g. Brandon",
            )

            mood = st.slider(
                label="Mood (1 = Low, 10 = High)",
                min_value=1,
                max_value=10,
                value=5,
            )

            update_text = st.text_area(
                label="What are you currently working on?",
                placeholder="e.g. Finishing the dashboard layout...",
                height=160,
            )

            blockers = st.text_area(
                label="Any blockers?",
                placeholder="e.g. Waiting on disclosures...",
                height=120,
            )

            submitted = st.form_submit_button(
                label="Submit Update",
                use_container_width=True,
            )

        if submitted:
            return {
                "name": name.strip(),
                "mood": mood,
                "update": update_text.strip(),
                "blockers": blockers.strip(),
                "timestamp": datetime.now().isoformat(),
            }

        return None

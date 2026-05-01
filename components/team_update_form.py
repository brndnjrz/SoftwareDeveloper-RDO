import streamlit as st
from datetime import datetime


# ── Timestamp Formatter ───────────────────────────────────────────────────────

def format_timestamp(dt: datetime) -> str:
    """
    Formats a datetime object into MM/DD/YYYY H:MMAM/PM display format.

    Input:  datetime(2026, 5, 1, 14, 25, 1)
    Output: "05/01/2026 2:25PM"

    Note:
        strftime("%I") produces a zero-padded hour  →  "02:25PM"
        .lstrip("0")   strips the leading zero       →  "2:25PM"
        This only affects single-digit hours, double digits are unaffected.
    """
    date_part = dt.strftime("%m/%d/%Y")               # "05/01/2026"
    time_part = dt.strftime("%I:%M%p").lstrip("0")    # "2:25PM"
    return f"{date_part} {time_part}"



# ── Validation ────────────────────────────────────────────────────────────────

def validate_form(name: str, mood: int, update_text: str) -> list[str]:
    """
    Validates required form fields and returns a list of error messages.
    An empty list means the submission is valid.

    Rules:
        - name       → required, letters/spaces only, 2–50 chars
        - mood       → must be an int between 1 and 10 (defensive check)
        - update     → required, must be at least 10 characters
    
    Note:
        blockers is intentionally excluded — it is optional by design.
        timestamp is generated internally, not user input, so not validated.
    """
    errors = []

    # ── Name ─────────────────────────────────────────────────────────────────
    if not name:
        errors.append("Name is required.")
    elif len(name) < 2:
        errors.append("Name must be at least 2 characters.")
    elif len(name) > 50:
        errors.append("Name must be 50 characters or fewer.")
    elif not all(char.isalpha() or char.isspace() for char in name):
        errors.append("Name can only contain letters and spaces.")

    # ── Mood ──────────────────────────────────────────────────────────────────
    if not isinstance(mood, int):
        errors.append("Mood must be a whole number.")
    elif not (1 <= mood <= 10):
        errors.append("Mood must be between 1 and 10.")

    # ── Update ────────────────────────────────────────────────────────────────
    if not update_text:
        errors.append("Please share current progress.")
    elif len(update_text) < 10:
        errors.append("Update must be at least 10 characters — add a bit more detail.")
    elif len(update_text) > 500:
        errors.append(f"Update is too long ({len(update_text)}/500 characters).")

    return errors


# ── Form ──────────────────────────────────────────────────────────────────────

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
        dict on valid submission, or None if not yet submitted or invalid.
    """

    with st.sidebar:
        st.header("New Update")

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

        # ── Validate before building the return dict ──────────────────────────
        if submitted:
            errors = validate_form(
                name=name.strip(),
                mood=mood,
                update_text=update_text.strip(),
            )

            if errors:
                for error in errors:
                    st.sidebar.error(error)
                return None
            
            now = datetime.now()

            return {
                "name": name.strip(),
                "mood": mood,
                "update": update_text.strip(),
                "blockers": blockers.strip(),
                "timestamp": now.isoformat(),            # "2026-05-01T14:25:01.815843"  → storage
                "timestamp_display": format_timestamp(now),  # "05/01/2026 2:25PM"          → display
            }

    return None

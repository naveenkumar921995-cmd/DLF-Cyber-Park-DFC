import streamlit as st
import pandas as pd
from database.db import init_db

# Initialize DB
init_db()

# Initialize session state safely
if "role" not in st.session_state:
    st.session_state.role = None

# Temporary Role Selector (for testing)
if st.session_state.role is None:
    st.title("Login")

    role = st.selectbox("Select Role", ["Admin", "User"])

    if st.button("Login"):
        st.session_state.role = role
        st.rerun()

# Admin Panel
if st.session_state.role == "Admin":
    st.title("Admin Dashboard")

    menu = st.sidebar.selectbox("Menu", [
        "Control Room",
        "Assets",
        "Work Logs",
        "Compliance",
        "Energy",
        "Attendance",
        "Purchase",
        "Reports"
    ])

    st.write(f"You selected: {menu}")

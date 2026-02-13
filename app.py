import streamlit as st
from database.db import init_db
from modules.assets import asset_page
from departments import department_page


# -------------------------
# Initialize Database
# -------------------------
init_db()

# -------------------------
# Session State Setup
# -------------------------
if "role" not in st.session_state:
    st.session_state.role = None

# -------------------------
# LOGIN SCREEN
# -------------------------
if st.session_state.role is None:

    st.title("DLF Cyber Park - Facility Management System")

    role = st.selectbox("Select Role", ["Admin", "User"])

    if st.button("Login"):
        st.session_state.role = role
        st.rerun()

# -------------------------
# ADMIN PANEL
# -------------------------
elif st.session_state.role == "Admin":

    st.sidebar.title("Navigation")

    menu = st.sidebar.selectbox("Menu", [
        "Dashboard",
        "Assets",
        "Departments",
        "Work Logs",
        "Compliance",
        "Energy",
        "Attendance",
        "Purchase",
        "Reports",
        "Logout"
    ])

    # -------------------------
    # DASHBOARD
    # -------------------------
    if menu == "Dashboard":
        st.title("🏢 Admin Dashboard")
        st.info("Welcome to Facility Management Control System")

    # -------------------------
    # ASSETS
    # -------------------------
    elif menu == "Assets":
        asset_page()

    # -------------------------
    # DEPARTMENTS
    # -------------------------
    elif menu == "Departments":

        dept_list = [
            "HVAC","Electrical","DG","STP","WTP",
            "Fire Fighting","CCTV & Access","Lifts",
            "BMS","Facade","Civil"
        ]

        selected_dept = st.selectbox(
            "Select Department",
            dept_list
        )

        department_page(selected_dept)

    # -------------------------
    # PLACEHOLDER MODULES
    # -------------------------
    elif menu == "Work Logs":
        st.title("Work Logs")
        st.warning("Module under development")

    elif menu == "Compliance":
        st.title("Compliance")
        st.warning("Module under development")

    elif menu == "Energy":
        st.title("Energy")
        st.warning("Module under development")

    elif menu == "Attendance":
        st.title("Attendance")
        st.warning("Module under development")

    elif menu == "Purchase":
        st.title("Purchase")
        st.warning("Module under development")

    elif menu == "Reports":
        st.title("Reports")
        st.warning("Module under development")

    # -------------------------
    # LOGOUT
    # -------------------------
    elif menu == "Logout":
        st.session_state.role = None
        st.rerun()

# -------------------------
# USER PANEL (Basic View)
# -------------------------
elif st.session_state.role == "User":

    st.title("User Dashboard")
    st.info("Limited access view")


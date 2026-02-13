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
    # -------------------------
    # HEADER WITH LOGOS
    # -------------------------
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("assets/dlf_logo.png", width=140)

    with col2:
        st.markdown(
            "<h2 style='text-align: center;'>DLF Cyber Park - Facility Management System</h2>",
            unsafe_allow_html=True
        )

    with col3:
        st.image("assets/lnp_logo.png", width=140)

    st.divider()

    # Header with Logos
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("assets/logo.png", width=120)

    with col2:
        st.markdown(
            "<h2 style='text-align: center;'>DLF Cyber Park Facility Management System</h2>",
            unsafe_allow_html=True
        )

    with col3:
        st.image("assets/logo.png", width=120)

    st.divider()

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

        st.title("🏢 Facility Control Room")

        from database.db import get_connection
        import pandas as pd

        conn = get_connection()

        # Total Assets
        total_assets_df = pd.read_sql(
            "SELECT COUNT(*) as count FROM assets",
            conn
        )
        total_assets = total_assets_df["count"][0]

        # Department-wise Count
        dept_data = pd.read_sql("""
            SELECT department, COUNT(*) as count
            FROM assets
            GROUP BY department
        """, conn)

        conn.close()

        # KPI Cards
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Assets", total_assets)

        with col2:
            st.metric("Active Departments", len(dept_data))

        st.divider()

        # Department Chart
        st.subheader("Assets by Department")

        if not dept_data.empty:
            st.bar_chart(
                dept_data.set_index("department")
            )
        else:
            st.info("No assets added yet.")

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
# USER PANEL
# -------------------------
elif st.session_state.role == "User":

    st.title("User Dashboard")
    st.info("Limited access view")



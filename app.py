import streamlit as st
from database.db import init_db, get_connection
from modules.assets import asset_page
from departments import department_page
import pandas as pd
from datetime import date


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

    # Header with Logos
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

    # Sidebar
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

        conn = get_connection()

        total_assets = pd.read_sql(
            "SELECT COUNT(*) as count FROM assets",
            conn
        )["count"][0]

        dept_data = pd.read_sql("""
            SELECT department, COUNT(*) as count
            FROM assets
            GROUP BY department
        """, conn)

        conn.close()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Assets", total_assets)

        with col2:
            st.metric("Active Departments", len(dept_data))

        st.divider()

        if not dept_data.empty:
            st.subheader("Assets by Department")
            st.bar_chart(dept_data.set_index("department"))
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

        selected_dept = st.selectbox("Select Department", dept_list)
        department_page(selected_dept)

    # -------------------------
    # WORK LOGS
    # -------------------------
    elif menu == "Work Logs":

        st.title("🛠 Work Log Entry")

        conn = get_connection()
        assets_df = pd.read_sql("SELECT asset_id, asset_name FROM assets", conn)

        if not assets_df.empty:

            selected_asset = st.selectbox(
                "Select Asset",
                assets_df["asset_name"].tolist()
            )

            work_date = st.date_input("Work Date", date.today())
            issue = st.text_area("Issue Description")
            action = st.text_area("Action Taken")

            if st.button("Save Work Log"):

                asset_id = assets_df[
                    assets_df["asset_name"] == selected_asset
                ]["asset_id"].values[0]

                conn.execute(
                    "INSERT INTO work_logs (asset_id, work_date, issue, action_taken) VALUES (?, ?, ?, ?)",
                    (asset_id, work_date, issue, action)
                )
                conn.commit()
                st.success("Work log saved!")

        else:
            st.warning("No assets available.")

        conn.close()

    # -------------------------
    # COMPLIANCE
    # -------------------------
    elif menu == "Compliance":

        st.title("📋 Compliance Tracker")

        conn = get_connection()

        dept = st.text_input("Department")
        activity = st.text_input("Activity")
        due_date = st.date_input("Due Date", date.today())
        status = st.selectbox("Status", ["Pending", "Completed"])

        if st.button("Save Compliance"):
            conn.execute(
                "INSERT INTO compliance (department, activity, due_date, status) VALUES (?, ?, ?, ?)",
                (dept, activity, due_date, status)
            )
            conn.commit()
            st.success("Saved successfully!")

        data = pd.read_sql("SELECT * FROM compliance", conn)
        st.dataframe(data)

        conn.close()

    # -------------------------
    # ENERGY
    # -------------------------
    elif menu == "Energy":

        st.title("⚡ Energy Monitoring")

        conn = get_connection()

        dept = st.text_input("Department")
        reading_date = st.date_input("Reading Date", date.today())
        units = st.number_input("Units Consumed", min_value=0.0)

        if st.button("Save Reading"):
            conn.execute(
                "INSERT INTO energy (department, reading_date, units) VALUES (?, ?, ?)",
                (dept, reading_date, units)
            )
            conn.commit()
            st.success("Reading saved!")

        data = pd.read_sql("SELECT department, units FROM energy", conn)

        if not data.empty:
            st.bar_chart(data.groupby("department").sum())

        conn.close()

    # -------------------------
    # ATTENDANCE
    # -------------------------
    elif menu == "Attendance":

        st.title("👷 Attendance Register")

        conn = get_connection()

        name = st.text_input("Employee Name")
        dept = st.text_input("Department")
        att_date = st.date_input("Date", date.today())
        status = st.selectbox("Status", ["Present", "Absent"])

        if st.button("Save Attendance"):
            conn.execute(
                "INSERT INTO attendance (employee_name, department, date, status) VALUES (?, ?, ?, ?)",
                (name, dept, att_date, status)
            )
            conn.commit()
            st.success("Attendance saved!")

        data = pd.read_sql("SELECT * FROM attendance", conn)
        st.dataframe(data)

        conn.close()

    # -------------------------
    # PURCHASE
    # -------------------------
    elif menu == "Purchase":

        st.title("🛒 Purchase Register")

        conn = get_connection()

        item = st.text_input("Item Name")
        dept = st.text_input("Department")
        qty = st.number_input("Quantity", min_value=1)
        p_date = st.date_input("Purchase Date", date.today())

        if st.button("Save Purchase"):
            conn.execute(
                "INSERT INTO purchase (item_name, department, quantity, date) VALUES (?, ?, ?, ?)",
                (item, dept, qty, p_date)
            )
            conn.commit()
            st.success("Purchase saved!")

        data = pd.read_sql("SELECT * FROM purchase", conn)
        st.dataframe(data)

        conn.close()

    # -------------------------
    # REPORTS
    # -------------------------
    elif menu == "Reports":

        st.title("📊 Reports")

        conn = get_connection()

        report_type = st.selectbox(
            "Select Table",
            ["assets", "work_logs", "compliance", "energy", "attendance", "purchase"]
        )

        data = pd.read_sql(f"SELECT * FROM {report_type}", conn)

        st.dataframe(data)

        st.download_button(
            "Download CSV",
            data.to_csv(index=False),
            file_name=f"{report_type}.csv",
            mime="text/csv"
        )

        conn.close()

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

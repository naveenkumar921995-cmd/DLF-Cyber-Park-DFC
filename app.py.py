if st.session_state["role"] == "Admin":
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

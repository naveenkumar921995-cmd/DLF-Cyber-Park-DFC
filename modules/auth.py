import streamlit as st
from database.db import get_connection

def login():
    st.title("DLF Cyber Park - Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            st.session_state["logged_in"] = True
            st.session_state["role"] = user[3]
            st.session_state["department"] = user[4]
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Credentials")

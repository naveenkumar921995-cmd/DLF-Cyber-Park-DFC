import streamlit as st
import pandas as pd
from database.db import get_connection

def department_page(selected_dept):
    st.title(f"{selected_dept} Department")

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM assets WHERE department=?",
        conn,
        params=(selected_dept,)
    )

    conn.close()

    if df.empty:
        st.warning("No assets found for this department.")
    else:
        st.success(f"Total Assets: {len(df)}")
        st.dataframe(df, use_container_width=True)

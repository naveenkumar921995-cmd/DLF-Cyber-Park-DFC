import streamlit as st
import pandas as pd
from database.db import get_connection


def asset_page():

    st.title("🏢 Asset Master Upload")

    uploaded_file = st.file_uploader(
        "Upload Asset Master Excel File",
        type=["xlsx"]
    )

    if uploaded_file is not None:

        df = pd.read_excel(uploaded_file)

        required_columns = [
            "asset_id",
            "asset_name",
            "department",
            "location"
        ]

        if all(col in df.columns for col in required_columns):

            conn = get_connection()
            cursor = conn.cursor()

            for _, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO assets (asset_id, asset_name, department, location)
                    VALUES (?, ?, ?, ?)
                """, (
                    row["asset_id"],
                    row["asset_name"],
                    row["department"],
                    row["location"]
                ))

            conn.commit()
            conn.close()

            st.success("✅ Assets Uploaded Successfully")

        else:
            st.error("Excel format incorrect. Please use proper template.")

    st.divider()

    # Show Current Assets
    st.subheader("Current Asset List")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM assets", conn)
    conn.close()

    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No assets available.")

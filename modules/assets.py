import streamlit as st
import pandas as pd
from database.db import get_connection


def asset_page():

    st.title("🏢 Asset Management")

    with st.expander("➕ Add New Asset", expanded=True):

        col1, col2 = st.columns(2)

        with col1:
            asset_id = st.text_input("Asset ID")
            department = st.selectbox(
                "Department",
                [
                    "HVAC","Electrical","DG","STP","WTP",
                    "Fire Fighting","CCTV & Access","Lifts",
                    "BMS","Facade","Civil"
                ]
            )

        with col2:
            asset_name = st.text_input("Asset Name")
            location = st.text_input("Location")

        if st.button("Save Asset"):
            if asset_id and asset_name:

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO assets (asset_id, asset_name, department, location)
                    VALUES (?, ?, ?, ?)
                """, (asset_id, asset_name, department, location))

                conn.commit()
                conn.close()

                st.success("✅ Asset Saved Successfully")

            else:
                st.error("Asset ID and Asset Name are required")

    st.divider()

    # Show all assets
    st.subheader("📋 All Assets")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM assets", conn)
    conn.close()

    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No assets added yet.")


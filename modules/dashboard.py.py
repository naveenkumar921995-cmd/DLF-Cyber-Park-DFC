from datetime import datetime
import pandas as pd

today = datetime.today()

df = pd.read_sql("SELECT * FROM compliance", conn)
df["expiry_date"] = pd.to_datetime(df["expiry_date"])

expiring = df[df["expiry_date"] <= today]

if not expiring.empty:
    st.error("⚠ Compliance Expired!")
    st.dataframe(expiring)

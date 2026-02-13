import sqlite3
import os

DB_PATH = "data/facility.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Departments Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)

    # Insert default departments only if empty
    cursor.execute("SELECT COUNT(*) FROM departments")
    count = cursor.fetchone()[0]

    if count == 0:
        departments = [
            ("HVAC",),
            ("Electrical",),
            ("DG",),
            ("STP",),
            ("WTP",),
            ("Fire Fighting",),
            ("CCTV & Access",),
            ("Lifts",),
            ("BMS",),
            ("Facade",),
            ("Civil",),
            ("Compliance",),
            ("Energy",),
            ("Stores",),
            ("Purchase",),
            ("Administration",)
        ]

        cursor.executemany(
            "INSERT INTO departments (name) VALUES (?)",
            departments
        )
# Assets Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id TEXT,
        asset_name TEXT,
        department TEXT,
        location TEXT
    )
""")

    conn.commit()
    conn.close()


import sqlite3
import os

DB_PATH = "data/facility.db"


def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # -------------------------
    # Departments Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)

    # Insert default departments if empty
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

    # -------------------------
    # Assets Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id TEXT,
            asset_name TEXT,
            department TEXT,
            location TEXT
        )
    """)

    # -------------------------
    # Work Logs Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER,
            work_date DATE,
            issue TEXT,
            action_taken TEXT
        )
    """)

    # -------------------------
    # Compliance Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compliance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT,
            activity TEXT,
            due_date DATE,
            status TEXT
        )
    """)

    # -------------------------
    # Energy Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS energy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT,
            reading_date DATE,
            units REAL
        )
    """)

    # -------------------------
    # Attendance Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT,
            department TEXT,
            date DATE,
            status TEXT
        )
    """)

    # -------------------------
    # Purchase Table
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchase (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            department TEXT,
            quantity INTEGER,
            date DATE
        )
    """)

    conn.commit()
    conn.close()

import sqlite3
import os

DB_PATH = "data/facility.db"

def get_connection():
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT,
        department TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id TEXT,
        asset_name TEXT,
        department TEXT,
        location TEXT,
        capacity TEXT,
        make TEXT,
        model TEXT,
        amc_expiry TEXT,
        criticality TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS work_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        shift TEXT,
        asset_id TEXT,
        department TEXT,
        work_type TEXT,
        priority TEXT,
        description TEXT,
        downtime REAL,
        spares TEXT,
        status TEXT,
        created_by TEXT
    )
    """)

    conn.commit()
    conn.close()

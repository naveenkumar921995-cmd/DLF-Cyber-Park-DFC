import sqlite3
import os

DB_PATH = "data/facility.db"

def get_connection():
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

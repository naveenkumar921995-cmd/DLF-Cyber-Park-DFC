import sqlite3

def get_connection():
    conn = sqlite3.connect("data/facility.db", check_same_thread=False)
    return conn

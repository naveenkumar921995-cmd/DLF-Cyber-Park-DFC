import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

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
            ("Electrical",),
            ("Mechanical",),
            ("Housekeeping",),
            ("Security",)
        ]
        cursor.executemany(
            "INSERT INTO departments (name) VALUES (?)",
            departments
        )

    conn.commit()
    conn.close()

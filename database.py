import sqlite3

def get_connection():
    conn = sqlite3.connect("jobs.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied TEXT,
            status TEXT DEFAULT 'applied'
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database and table created!")
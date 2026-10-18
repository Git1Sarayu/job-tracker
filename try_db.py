from database import get_connection

conn = get_connection()

conn.execute(
    "INSERT INTO applications (company, role, date_applied, status) VALUES (?, ?, ?, ?)",
    ("Limish", "Python Developer", "2026-10-19", "applied")
)
conn.commit()

rows = conn.execute("SELECT * FROM applications").fetchall()
for row in rows:
    print(row["id"], row["company"], row["role"], row["date_applied"], row["status"])

conn.close()
import sqlite3

# Create a new SQLite DB (or connect if exists)
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    month TEXT PRIMARY KEY,
    present_days INTEGER,
    total_days INTEGER
)
""")

# Sample dummy data (Jan–Dec)
data = [
    ("January", 20, 22),
    ("February", 18, 20),
    ("March", 21, 23),
    ("April", 19, 21),
    ("May", 20, 22),
    ("June", 17, 22),
    ("July", 22, 23),
    ("August", 18, 21),
    ("September", 20, 22),
    ("October", 21, 22),
    ("November", 19, 21),
    ("December", 20, 22)
]

# Insert data (ignore duplicates)
cursor.executemany("INSERT OR IGNORE INTO attendance VALUES (?, ?, ?)", data)

conn.commit()
conn.close()

print("✅ Database created with sample attendance data!")

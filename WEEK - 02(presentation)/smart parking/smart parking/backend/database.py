import sqlite3

conn = sqlite3.connect("parking.db")

cursor = conn.cursor()

# Create parking slots table
cursor.execute("""
CREATE TABLE IF NOT EXISTS parking_slots(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slot_number TEXT,
    status TEXT
)
""")

# Create bookings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    vehicle TEXT,
    slot TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
import sqlite3

conn = sqlite3.connect("parking.db")
cursor = conn.cursor()

slots = [
    ("A1", "Available"),
    ("A2", "Available"),
    ("A3", "Occupied"),
    ("B1", "Available"),
    ("B2", "Occupied")
]

cursor.executemany(
    "INSERT INTO parking_slots (slot_number, status) VALUES (?, ?)",
    slots
)

conn.commit()
conn.close()

print("Parking slots added successfully!")
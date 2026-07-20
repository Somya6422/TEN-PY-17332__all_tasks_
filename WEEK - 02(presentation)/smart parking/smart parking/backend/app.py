from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Smart Car Parking Backend is Running!"


@app.route("/slots")
def get_slots():

    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM parking_slots")
    rows = cursor.fetchall()

    conn.close()

    slots = []

    for row in rows:
        slots.append({
            "id": row[0],
            "slot_number": row[1],
            "status": row[2]
        })

    return jsonify(slots)


@app.route("/book", methods=["POST"])
def book_slot():

    data = request.get_json()

    name = data["name"]
    vehicle = data["vehicle"]
    slot = data["slot"]

    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    # Check if the slot is already occupied
    cursor.execute(
        "SELECT status FROM parking_slots WHERE slot_number=?",
        (slot,)
    )

    result = cursor.fetchone()

    if result is None:
        conn.close()
        return jsonify({"message": "Slot not found!"})

    if result[0] == "Occupied":
        conn.close()
        return jsonify({"message": "❌ This slot is already occupied!"})

    # Save booking
    cursor.execute(
        "INSERT INTO bookings(name, vehicle, slot) VALUES (?, ?, ?)",
        (name, vehicle, slot)
    )

    # Update slot status
    cursor.execute(
        "UPDATE parking_slots SET status='Occupied' WHERE slot_number=?",
        (slot,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": f"Booking Confirmed for {name} ({vehicle}) at Slot {slot}"
    })


if __name__ == "__main__":
    app.run(debug=True)
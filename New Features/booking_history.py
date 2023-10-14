# booking_history.py
import sqlite3

def get_booking_history(username):
    conn = sqlite3.connect('bus_database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM bookings WHERE username=?", (username,))
    booking_history = cursor.fetchall()
    
    conn.close()
    return booking_history

# Usage
username = "user123"
booking_history = get_booking_history(username)
print("Booking History:")
for booking in booking_history:
    print(booking)

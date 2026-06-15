import sqlite3

def get_connection():
    return sqlite3.connect("bookings.db")
    

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               passenger_name TEXT,
               departure_city TEXT,
               destination_city TEXT,
               travel_date TEXT,
               seat_number TEXT,
               ticket_price REAL,
               status TEXT
               
               
               )
""")


def add_booking(passenger_name, departure_city, destination_city, travel_date, seat_number, ticket_price, status="booked"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bookings
    (passenger_name, departure_city, destination_city, travel_date, seat_number, ticket_price, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (passenger_name, departure_city, destination_city, travel_date, seat_number, ticket_price, status))
    
    conn.commit()
    conn.close()

def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()

    conn.close()
    return bookings

def get_booking_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings WHERE id = ?", 
                   (id,))
    booking_by_id = cursor.fetchone()
    conn.close()
    return booking_by_id

def delete_booking(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM bookings WHERE id = ?",
                   (id,))
    
    conn.commit()
    conn.close()
    print(f"Number {id} Booking has been deleted.")

def update_booking_status(id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE bookings SET status = ? WHERE id = ? ", (status, id))
    
    conn.commit()
    conn.close()
    print(f'ID - {id} ticket is now {status}')






conn.commit()
conn.close()


from flask import Flask, jsonify, request
from database import get_all_bookings, get_booking_by_id, add_booking, update_booking_status, delete_booking

app = Flask(__name__)

@app.route("/")
def home():
    return "Ticket Booking Automation System"

@app.route("/bookings")
def bookings():
    data = get_all_bookings()
    return jsonify(data)

@app.route("/bookings/<int:id>")
def booking_by_id(id):
    data = get_booking_by_id(id)

    if data is None:
        return jsonify({"error": "Booking not found"}), 404

    return jsonify(data)

@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    passenger_name = data.get("passenger_name")
    destination_city = data.get("destination_city")
    departure_city = data.get("departure_city")
    travel_date = data.get("travel_date")
    seat_number = data.get("seat_number")
    ticket_price = data.get("ticket_price")

    add_booking(
        passenger_name,
        departure_city,
        destination_city,
        travel_date,
        seat_number,
        ticket_price
    )

    return jsonify({"message": "booking created succesfuly"}), 201

@app.route("/bookings/<int:id>", methods=["PUT"])
def update_booking(id):
    data = request.get_json()
    status = data.get("status")


    update_booking_status(
        id,
        status
    )
    return jsonify({"message":"status updated succesfuly"}), 200

@app.route('/bookings', methods=["DELETE"])
def delete_booking(id):
    data = request.get_json()




if __name__ == "__main__":
    app.run(debug=True)

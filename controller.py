"""This file is for implement logics and web application with Flask"""
from datetime import datetime
from flask import Flask
from models import BookingDataAccess

app = Flask(__name__)


"""
[GET] /ping
Returns pong if the back-end is live

[GET] /booking/{seat}/{date}
Returns the given seat at the given date

[PUT] /booking/{seat}/book_dates{?date_from=}{?date_to=}{?username=}
("username" of the person who booked the seat, "date_from", "date_to")
Books the given seat at multiple dates

[PUT] /booking/{seat}/cancel{?date=}
Cancels the given booking at the specified date

[PUT] /seat/update{?seat_id=} (Body: seat object)
Updates the given seat

[POST] /login (header: username, password)
Authenticates the user, returns user or if you want bearer-token

[POST] /seat/create (Body: seat)
Creates and registers a new seat

[DELETE] /seat/delete{?seat_id=}
Deletes the given seat*date: in ISO Format String: yyyy-MM-dd
"""


@app.route("/booking/seat/date")
def booking_seat():
    """[PUT] /booking/{seat}/date{?username=}
    Books the given seat at a certain date


    """
    bda = BookingDataAccess()
    bda.create(date, username, seat_id)
    return True


@app.route("/booking/list/<date>", methods=["GET"])
def booking_list_date(date):
    """[GET] /booking/list/{date}
    Returns a seat list with all seats at the given date

    :param date:

    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except:
        return "bad time format"


@app.route("/booking/seat/date")
def booking_seat():
    """[PUT] /booking/{seat}/book_dates{?date_from=}{?date_to=}{?username=}
    ("username" of the person who booked the seat, "date_from", "date_to")
    Books the given seat at multiple dates


    """
    pass


@app.route("/booking/seat/date")
def booking_seat():
    """[PUT] /booking/{seat}/cancel{?date=}
    Cancels the given booking at the specified date


    """
    pass


@app.route("/booking/seat/date")
def booking_seat():
    """[PUT] /seat/update{?seat_id=} (Body: seat object)
    Updates the given seat


    """
    pass


@app.route("/booking/seat/date")
def booking_seat():
    """[POST] /login (header: username, password)
    Authenticates the user, returns user or if you want bearer-token


    """
    pass


@app.route("/booking/seat/date")
def booking_seat():
    """[POST] /seat/create (Body: seat)
    Creates and registers a new seat


    """
    pass


@app.route("/booking/seat/date")
def booking_seat():
    """[DELETE] /seat/delete{?seat_id=}
    Deletes the given seat*date: in ISO Format String: yyyy-MM-dd


    """
    pass


@app.route("/booking/seat/date")
def booking_seat():
    """[GET] /booking/{seat}/{date}
    Returns the given seat at the given date


    """
    pass


@app.route("/pong",methods=['GET'])
def pong():
    """[GET] /ping
    Returns pong if the back-end is live


    """
    return "pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

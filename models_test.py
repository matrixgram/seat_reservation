# test booking.read_all()
from models import BookingDataAccess as bda, UserDataAccess as uda, \
DatabaseManager as dbm
from models import SeatDataAccess as sda
import pandas as pd
import sqlite3

# create user
# assert uda.create() == True
# create seat
# create booking
# read_all booking
# assert bda.read_all() == pd.read_excel('Agent Dummy Data.xlsx')

### Testing
# c.execute("""SELECT COUNT(*) FROM employees """)
# c.execute("""SELECT * FROM employees WHERE role='Admin' """)
# print(c.fetchone())
# print(len(c.fetchall()))

## Print list of tables
# c.execute("""SELECT * from SQLITE_MASTER WHERE type='table'""")
# print(c.fetchall())
# c.close()

#test UserDataAccess
db_file = r'C:\Users\Hessam\Documents\TechLabs\Data Science Track\Project\TechLabs-Seat-Booking-Tool\back-end\test(2).db'
db = dbm(db_file)
users = uda()

# print(users.read(db_file, "ackermann.61"))
# print(users.read_all(db_file))

# users.delete(db_file, "ackermann.61")
# print(users.read(db_file, "ackermann.61"))

# print(users.update(db_file, ("Hess","rmz","Dort","emp",'asdsads')))
# print(users.read(db_file, "amsel.12"))


#test SeatDataAccess
seats = sda()
# assert seats.create(db_file,'seat_id', 'name', 'status', 'position') == True
# print(seats.create(db_file,'seat_id', 'name', 'status', 'position'))

# print(seats.read(db_file, 'seat_id'))
# print(seats.read_all(db_file))

# print(seats.update(db_file, ("Hess","rmz","Dort")))
# print(seats.read(db_file, "seat_id"))

# print(seats.delete(db_file, 'seat_id'))
# print(seats.read(db_file, "seat_id"))



#test BookingDataAccess
bks = bda()
# assert bks.create(db_file,'date', 'user', 'seat') == True
# print(seats.create(db_file,'seat_id', 'name', 'status', 'position'))

# print(bks.read(db_file, 'date3', 'user3', 'seat3'))
# print(bks.read_all(db_file))

# print(bks.update(db_file, ("date3","user3","Dort")))
# print(bks.read(db_file, "date3","rmz","Dort"))

# print(bks.delete(db_file, 'date3', 'user3', 'seat3'))
# print(bks.read(db_file, 'date3', 'user3', 'seat3'))



    
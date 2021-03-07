""" This file for implement data access."""
import sqlite3

DB_ADDRESS = "test.db"


class DatabaseManager:
    """ It is for DB access """

    def __init__(self, db_address=DB_ADDRESS):
        try:
            self.connection = sqlite3.connect(f"file:{db_address}?mode=rw", uri=True)
        except sqlite3.OperationalError:
            # database not exist
            self.connection = sqlite3.connect(db_address)
            self.connection.execute(
                """
                CREATE TABLE users (
                username text NOT NULL PRIMARY KEY,
                first_name text,
                last_name text,
                city text,
                role text
                )
                """
            )
            self.connection.execute(
                """
                CREATE TABLE seats (
                seat_id text NOT NULL PRIMARY KEY,
                status text
                )
                """
            )
            self.connection.execute(
                """
                CREATE TABLE bookings (
                date text,
                username text,
                seat_id text,
                PRIMARY KEY (date, username, seat_id)
                )
                """
            )


class UserDataAccess:
    """ Access to Users table """
    
    
    def create(self, db_file, username, first_name, last_name, role, city):
        try:
            db = DatabaseManager(db_file)
            db.connection.execute(
                "INSERT INTO users (username, first_name, last_name, role, city) VALUES (%s, %s, %s, %s, %s)",
                (username, first_name, last_name, role, city)
            )
            db.connection.commit()
            db.connection.close
            return True
        except sqlite3.IntegrityError:
            return False

    def read(self, db_file, username):
        """
        Reads and returns user records

        Parameters
        ----------
        db_file : db file path.
        username : string.

        Returns
        -------
        matching records

        """
        db = DatabaseManager()
        conn = db.connection
        inq = conn.execute("SELECT * FROM employees WHERE username=?", (username,))
        return inq.fetchall()

        
    def read_all(self, db_file):
        """
        Reads all the available user data

        """
        db = DatabaseManager(db_file)
        inq = db.connection.execute("SELECT * FROM employees")
        return inq.fetchall()
    
    def update(self, db_file, user_info):
        """
         Updates a user record using username

        Parameters
        ----------
        db_file : database file.
        user_info : tuple of user information 
        with shape (first, last, city, username, role).

        """
        # db = DatabaseManager(db_file)
        conn = sqlite3.connect(db_file)
        # conn = db.connect()
        cur = conn.cursor()
        with conn:
            cur.execute("""UPDATE employees
                         SET first = ?,
                             last = ?,
                             city = ?,
                             role = ?,
                             pass = ?""", user_info)

        
    def delete(self, db_file, username):
        """
        Deletes a user record using username

        """
        db = DatabaseManager(db_file)
        conn = db.connection
        with conn:
            conn.execute("DELETE FROM employees WHERE username=?", (username,))
  
    

class SeatDataAccess:
    """ Creates access to seat data
    """
    def create(self, db_file, seat_id, name, status, position, username= 'NULL'):
        """
        Creates a new seat record

        """
        try:
            db = DatabaseManager(db_file)
            db.connection.cursor().execute(
                "INSERT INTO seats (seat_id, name, status, position, username) VALUES (?, ?, ?, ?, ?)",
                (seat_id, name, status, position, username)
            )
            db.connection.commit()
            db.connection.close
            return True
        except sqlite3.IntegrityError:
            return False
    
    def read(self, db_file, seat_id):
        """
        Reads and returns seats records

        Parameters
        ----------
        db_file : db file path.
        seat_id : string.

        Returns
        -------
        matching records

        """
        db = DatabaseManager(db_file)
        conn = db.connection
        inq = conn.execute("SELECT * FROM seats WHERE seat_id=?", (seat_id,))
        return inq.fetchall()
    
    def read_all(self, db_file):
        """
        Reads all the available seats data

        """
        db = DatabaseManager(db_file)
        inq = db.connection.execute("SELECT * FROM seats")
        return inq.fetchall()
    
    def update(self, db_file, seat_info):
        """
         Updates a seat record using seat_id. Note that seat_id is a primary key
         and username is a foriegn key and cannot be modified.

        Parameters
        ----------
        db_file : database file.
        user_info : tuple of user information 
        with shape (name, status, position).

        """
        # db = DatabaseManager(db_file)
        conn = sqlite3.connect(db_file)
        # conn = db.connect()
        cur = conn.cursor()
        with conn:
            cur.execute("""UPDATE seats
                         SET name = ?,
                             status = ?,
                             position = ?
                             """, seat_info)
                             
    
    def delete(self, db_file, seat_id):
        """
        Deletes a seat record using seat_id

        """
        db = DatabaseManager(db_file)
        conn = db.connection
        with conn:
            conn.execute("DELETE FROM seats WHERE seat_id=?", (seat_id,))



class BookingDataAccess:
    """ """

    def create(self, db_file, date, username, seat_id):
        try:
            db = DatabaseManager(db_file)
            db.connection.execute(
                "INSERT INTO bookings (date, username, seat_id) VALUES (?, ?, ?)",
                (date, username, seat_id))
            db.connection.commit()
            db.connection.close
            return True
        except sqlite3.IntegrityError:
            return False

    def read(self, db_file, date, username, seat_id):
        """
        Reads and returns bookings records

        """
        db = DatabaseManager(db_file)
        conn = db.connection
        inq = conn.execute("""SELECT * FROM bookings WHERE 
                           date=? AND username=? AND seat_id=?""", 
                           (date, username, seat_id))
        return inq.fetchall()
    
    def read_all(self, db_file):
        """
        Reads all the available bookings

        """
        db = DatabaseManager(db_file)
        inq = db.connection.cursor().execute("SELECT * FROM bookings")
        return inq.fetchall()
    
    
    
    ### Issue: Bookings cannot be updated
    ### Possible cause: handling primary keys
    
    def update(self, db_file, book_info):
        """
          Updates a booking record using book_info

        Parameters
        ----------
        db_file : database file.
        user_info : tuple of user information 
        with shape (name, status, position).

        """
        # db = DatabaseManager(db_file)
        conn = sqlite3.connect(db_file)
        # conn = db.connect()
        cur = conn.cursor()
        with conn:
            cur.execute("""UPDATE bookings
                          SET date = ?,
                              username = ?,
                              seat_id = ?
                              """, book_info)
                             
    
    def delete(self, db_file, date, username, seat_id):
        """
        Deletes a seat record using seat_id

        """
        db = DatabaseManager(db_file)
        conn = db.connection
        with conn:
            conn.execute("""DELETE FROM bookings WHERE 
                         date=? AND username=? AND seat_id=?""", (date, username, seat_id))
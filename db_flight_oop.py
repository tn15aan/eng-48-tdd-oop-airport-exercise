import pyodbc
from db_connect_oop import *

class AEFlights(MSDBConnection):
    def print_all(self):
        query = 'SELECT * FROM Flight'
        data = self._MSDBConnection__sql_query(query)
        return data

    def set_id(self):
        id = int(input('Select an ID'))
        return id

    def read_one(self, id):
        query = f"SELECT * FROM Flight WHERE flightID = {id}"
        result = self._MSDBConnection__sql_query(query)
        return result
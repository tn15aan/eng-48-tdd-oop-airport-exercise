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

    #Creating a passenger
    def set_passenger_id(self):
        passenger_id = int(input('Select ID for passenger'))
        return passenger_id
    #
    def set_passenger_name(self):
        passenger_name = input('Select name for passenger')
        return passenger_name

    def set_passport_num(self):
        passport_num = input('Enter the passport number')
        return passport_num

    def add_passenger(self, passenger_id, passenger_name, passport_num):
        # passenger_name = input('Select name for passenger')
        # passport_num = input('Enter the passport number')
        query = f"INSERT INTO Passenger VALUES({passenger_id}, '{passenger_name}', '{passport_num}')"
        result = self._MSDBConnection__sql_query(query)
        self.docker_AirportEx.commit()
        return result

# table_flights = AEFlights()
#
# passenger_id = table_flights.set_passenger_id()
# passenger_name = table_flights.set_passenger_name()
# passport_num = table_flights.set_passport_num()
# passenger_1 = table_flights.add_passenger(passenger_id, passenger_name, passport_num)


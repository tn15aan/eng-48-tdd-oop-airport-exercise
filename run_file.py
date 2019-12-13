from passengers_class import *
from flight_trip_class import *
from db_flight_oop import *
flight_table = AEFlights()


while True:
    print('Choose your option')
    print('1 - Print all flights')
    print('2 - Check for flight using a flight ID')
    print('3 - Create a passenger (INSERT)')
    print('4 - Add a passenger to a flight (ALTER / UPDATE)')
    userInput = input('Enter your option number: ')
    if userInput == '1':
        # print('Create a passenger')
        # passengerName = input('Enter the passengers name')
        # passportNum = input('Enter the passport number')
        # newPassenger = passengerName, passportNum
        # add_passenger(newPassenger)
        print_flight = flight_table.print_all()
        print(print_flight.fetchall())
    elif userInput == '2':
        id = flight_table.set_id()
        read_flight = flight_table.read_one(id)
        print(read_flight.fetchone())
    elif userInput == '3':
        passenger_id = flight_table.set_passenger_id()
        passenger_name = flight_table.set_passenger_name()
        passport_num = flight_table.set_passport_num()
        print('Passenger successfully added')
        passenger_1 = flight_table.add_passenger(passenger_id, passenger_name, passport_num)
        break
    elif userInput == '4':
        pass
    elif 'bye' in userInput or 'exit' in userInput:
        print('Goodbye! Thank you')
        break
    else:
        print("I didn't quite catch that. Please choose a valid option")

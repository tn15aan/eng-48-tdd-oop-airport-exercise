from passengers_class import *
from plane_class import *
from flight_trip_class import *

def test_initializing_passenger():
    # Setup
    passenger1 = Passenger('Joana Thomson', 'B343123')
    passenger2 = Passenger('Birt Kuman', 'B13927')
    # Assertion
    assert passenger1.passportNum == 'B343123'
    assert passenger2.passportNum == 'B13927'
    assert passenger1.name == 'Joana Thomson'
    assert passenger2.name == 'Birt Kuman'

def test_initializing_plane():
    # Setup
    plane1 = Plane('BA4534')
    plane2 = Plane('CP7543')
    # Assertion
    assert plane1.planeNumber == 'BA4534'
    assert plane2.planeNumber == 'CP7543'

def test_Flight():
    new_trip = Flight_Trip()
    assert isinstance(new_trip, Flight_Trip)

def test_plane():
    plane1 = Plane('BA3454')
    assert isinstance(plane1, Plane)

def test_flight_plane():
    new_trip = Flight_Trip()
    new_trip.add_plane('BA2221')
    assert new_trip.plane == 'BA2221'

def test_flight_destination():
    new_trip = Flight_Trip()
    new_trip.add_destination('London')
    assert new_trip.destination == ('London')

def test_flight_origin():
    new_trip = Flight_Trip()
    new_trip.add_origin('Berlin')
    assert new_trip.origin == ('Berlin')

def test_list_of_passengers():
    new_trip = Flight_Trip()
    new_trip.add_passenger('Jerome')
    assert new_trip.passengers[0] == ('Jerome')
    assert type(new_trip.passengers) == type([])

def test_passenger_error():
    try:
        Passenger()
    except TypeError as error:
        print('Have you passed through the passengers name and passport number?')




# from flight_trip_class import *
#
# flightTrip1 = Flight_Trip('BA4534', 'Berlin', 'London', 'Joana Thomson')
# flightTrip2 = Flight_Trip('B13927', 'Moscow', 'Paris', 'Birt Kuman')
#
# print(flightTrip1.name)

# print(passenger1.passportNum)
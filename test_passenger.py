from passengers_class import *


def test_initializing_passenger():
    # Setup
    passenger1 = Passenger('Joana Thomson', 'B343123')
    passenger2 = Passenger('Birt Kuman', 'B13927')
    # Assertion
    assert passenger1.passportNum == 'B343123'
    assert passenger2.passportNum == 'B13927'
    assert passenger1.name == 'Joana Thomson'
    assert passenger2.name == 'Birt Kuman'


# print(passenger1.passportNum)
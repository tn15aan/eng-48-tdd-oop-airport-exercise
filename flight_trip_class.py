from passengers_class import *
from plane_class import *

class flight_trip():
    def __init__(self, planeNumber, destination, origin, name):
        super().__init__(planeNumber, name)
        self.destination = destination
        self.origin = origin
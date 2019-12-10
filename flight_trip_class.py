class Flight_Trip():
    def __init__(self): #'self' is an instance of an object
        self.plane = ''
        self.destination = ''
        self.origin = ''
        self.passengers = []

    def add_plane(self, plane_num):
        self.plane = plane_num

    def add_destination(self, destination_name):
        self.destination = destination_name

    def add_origin(self,origin_name):
        self.origin = origin_name

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

# from passengers_class import *
# from plane_class import *
#
# class Flight_Trip(Passenger, Plane):
#     def __init__(self, planeNumber, destination, origin, name):
#         self.planeNumber = ''
#         self.destination = ''
#         self.origin = ''
#         self
#
#     def add_plane(self, plane_number):
#         self.plane_number = plane_number
#
#     def add_destination(self, destination):
#         self.destination = destination
#
#     def add_origin(self, origin):
#         self.origin = origin

class Passenger():

    def __init__(self, name, passportNum):
        self.name = name
        self.passportNum = passportNum

    # class_variable = ['peanuts']
    # def __init__(self):
    #     Passenger.class_variable.append(self)
    #
    # passenger1 = Passenger('Fred')
    # print(Passenger.class_variable)
    # print(Passenger.class_variable[1].name)

#     def add_passenger(self):
#         passengerList = []
#         name = input('Please enter a name')
#         passportNum = input('Please enter a passport number')
#         newPassenger = name, passportNum
#         passengerList.append(newPassenger)
#         print(passengerList)
#
# Passenger.add_passenger('hi')
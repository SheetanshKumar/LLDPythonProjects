class UserController(object):
    def __init__(self, userService):
        self.userService = userService

    def addUser(self, id, name):
        return self.userService.addUser(id, name)

    def addBooking(self, id, name, location, slots, gymController):
        if id not in self.userService.__class__.userDetails:
            return "User Not registered"

        # user = self.userService.__class__.userDetails[id]
        # user.setBookings(slots)
        # self.userService.__class__.userDetails[id] = user
        gymdetails = gymController.gymService.__class__.gymDetails
        if location not in gymdetails:
            return "location not present"

        gym = gymdetails[location]
        type = list(slots.keys())[0]
        available = gym.getSlots()
        if type not in available:
            return "slot not available for {}".format(type)


        available = available[type]
        if slots[type][0] >= available[0] and slots[type][1] <= available[1] and available[2] > 0:
            # gymController.addGym('2', 'Bellaundur', {"Cardio": (7, 8, 150)})
            res = self.userService.addUserBookings(id, name, location, slots)
            if not res[1]:
                return res[0]
            s = {type: (available[0], available[1], available[2] - 1)}
            gymController.addGym(id, location, s)
            return "Booking confirmed"


        return "Booking not confirmed, slots not availabe"

    def getUserBookings(self, id, name):
        return self.userService.getUserBookings(id, name)
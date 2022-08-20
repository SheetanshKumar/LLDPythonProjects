from services.user_service_interface import UserServiceInterface
from services.gym_service import GymService
from models.user import User


class UserService(UserServiceInterface):
    # adding class level dictionary to set it in the db, here it is in-memory
    userDetails = {}

    def addUser(self, id, name):
        user = User()
        user.setId(id)
        user.setId(name)
        user.setBookings([])
        self.__class__.userDetails[id] = user
        return user

    def addUserBookings(self, id, name, location, slots):

        if id not in self.__class__.userDetails:
            return ("User not registered", False)
        user = self.__class__.userDetails[id]
        bookings = self.getUserBookings(id, name)

        flag = 1
        for i in range(len(bookings)):
            workouttypeslot = list(slots.keys())[0]
            workouttypebooking = list(bookings[i].keys())[0]

            if slots[workouttypeslot][0] == bookings[i][workouttypebooking][0]:
                flag = 0
                if user.getType() == "Premium":
                    bookings.pop(i)
                    bookings.append(slots)
                    break
                else:
                    print("user not premiuim")
                    return ("User not Premium, Overwriting not allowed", False)
        if flag:
            bookings.append(slots)
        user.setBookings(bookings)
        # print("booking=", bookings)
        # print(bookings)
        if len(bookings) >= 3:
            user.setType("Premium")
        self.__class__.userDetails[id] = user
        return ("Booking done", True)


    def getUserBookings(self, id, name):
        user = self.__class__.userDetails[id]
        return user.getBookings()
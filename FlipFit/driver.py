from controllers.user_controller import UserController
from controllers.gymController import GymController

from services.user_service import UserService
from services.gym_service import GymService

userController = UserController(UserService())
gymController = GymController(GymService())

gymController.addGym('1', 'Kormangala', {"Weights": (6, 7, 100)})
gymController.addGym('1', 'Kormangala', {"Cardio": (7, 8, 150)})
gymController.addGym('1', 'Kormangala', {"Yoga": (8, 9, 200)})
# gymController.addGym('1', 'Kormangala', {"Cardio": (6, 7, 150)})
# gymController.addGym('1', 'Kormangala', {"Yoga": (6, 7, 150)})
gymController.addGym('1', 'Kormangala', {"Weights": (8, 9, 150)})

gymController.addGym('2', 'Bellaundur', {"Cardio": (7, 8, 150)})
gymController.addGym('2', 'Bellaundur', {"Yoga": (8, 9, 200)})

# gymController.addGym('1', 'Kormangala', {"Weights": (6, 7, 100)})
# gymController.addGym('1', 'Kormangala', {"Cardio": (7, 8, 150)})
# gymController.addGym('1', 'Kormangala', {"Yoga": (8, 9, 200)})
#
# gymController.addGym('2', 'Bellaundur', {"Cardio": (7, 8, 150)})
# gymController.addGym('2', 'Bellaundur', {"Yoga": (8, 9, 200)})

print(gymController.getSlots())

userController.addUser('1', "Sheetansh")
print(userController.addBooking('1', "Sheetansh", 'Kormangala', {"Weights": (6, 7, 'Monday')}, gymController))
print(gymController.getSlots())


print(userController.getUserBookings('1', 'Sheetansh'))
# print(userController.getUserBookings('2', 'Rahul'))

# print(userController.addBooking('1', "Sheetansh", 'Kormangala', {"Weights": (6, 7, 'Monday')}, gymController))
# print(userController.addBooking('3', "name", 'Kormangala', {"Weights": (6, 7, 'Monday')}, gymController))

print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Cardio": (7,8, 'Monday')}, gymController))
print(userController.getUserBookings('1', 'Sheetansh'))
print(gymController.getSlots())
#
# print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Weights": (8,9, 'Monday')}, gymController))
# print(userController.getUserBookings('1', 'Sheetansh'))
# print(gymController.getSlots())
# print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Cardio": (6 ,7, 'Monday')}, gymController))
# print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Cardio": (7,8, 'Monday')}, gymController))
# print(userController.getUserBookings('1', 'Sheetansh'))
# print(gymController.getSlots())


# print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Yoga": (7, 8, 'Monday')}, gymController))
# print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Weights": (8, 9, 'Monday')}, gymController))
# print(userController.addBooking('1', "sheetansh", 'Kormangala', {"Cardio": (8, 9, 'Monday')}, gymController))
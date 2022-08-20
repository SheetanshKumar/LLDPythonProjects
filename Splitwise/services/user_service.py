from services.user_service_interface import UserServiceInterface
from models.user import User


class UserService(UserServiceInterface):
    # adding class level dictionary to set it in the db, here it is in-memory
    userDetails = {}

    def addUser(self, id, name):
        user = User()
        user.setId(id)
        user.setId(name)

        self.__class__.userDetails[id] = user
        return user

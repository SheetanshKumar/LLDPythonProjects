import abc

class UserServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self, id, name):
        pass

    @abc.abstractmethod
    def addUserBookings(self, id, name, location, booking):
        pass

    @abc.abstractmethod
    def getUserBookings(self, id, name):
        pass
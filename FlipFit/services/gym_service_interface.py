import abc

class GymServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addGym(self, id, name, slots):
        pass

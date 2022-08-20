import abc

class ContactServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addNewContact(self, id, firstname, lastname, phone):
        pass

    @abc.abstractmethod
    def updateContact(self, id, firstname, lastname, phone):
        pass


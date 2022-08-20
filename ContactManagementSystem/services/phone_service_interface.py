import abc


class PhoneServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getPhoneObject(self, phonenumber):
        pass
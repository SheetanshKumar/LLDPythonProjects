class PhoneController(object):

    def __init__(self, phoneService):
        self.phoneService = phoneService

    def getPhoneObject(self, phone):
        return self.phoneService.getPhoneObject(phone)
from services.phone_service_interface import PhoneServiceInterface
from models.phone import Phone


class PhoneService(PhoneServiceInterface):

    def getPhoneObject(self, phonenumber):
        phone = Phone()
        phone.setPhone(phonenumber)
        phone.setCountryCode("Default")
        return phone

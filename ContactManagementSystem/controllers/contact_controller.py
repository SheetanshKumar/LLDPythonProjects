from utils.search_util import Search
from utils.validation_util import Validate
from controllers.phone_controller import PhoneController
from services.phone_service import PhoneService


class ContactController(object):

    def __init__(self, contactService):
        self.contactService = contactService
        self.phoneController = PhoneController(PhoneService())
        self.validate = Validate()
        self.search = Search()

    def addNewContact(self, id, firstname, lastname, phone):
        if not self.validate.validatePhoneNumber(phone):
            return "Invalid Phone Number"
        if id in self.contactService.contacts:
            return "Error: contact id does already exist"
        phone = self.phoneController.getPhoneObject(phone)
        return self.contactService.addNewContact(id, firstname, lastname, phone)

    def updateContact(self, id, firstname, lastname, phone):
        if not self.validate.validatePhoneNumber(phone):
            return "Invalid Phone Number"
        if id not in self.contactService.contacts:
            return "Error: contact id does not exist"
        phone = self.phoneController.getPhoneObject(phone)
        return self.contactService.updateContact(id, firstname, lastname, phone)

    def searchByType(self, item, type):
            if type == "firstname":
                return self.searchByFirstName(item)
            elif type == "lastname":
                return self.searchByLastName(item)
            elif type == "phonenumber":
                return self.searchByPhoneNumber(item)
            else:
                return "ERROR: wrong type mentioned in the search"

    def searchByFirstName(self, item):
        if not self.searchByTrieFirstName(item):
            return 0, []
        contacts = self.contactService.contacts
        ids = list(self.contactService.contacts.keys())
        result = []
        for id in ids:
            contact = contacts[id]
            if self.search.searchInStringPrefix(item, contact.getFirstName()):
                result.append(
                    ([contact.getId(), contact.getFirstName(), contact.getLastName(), contact.getPhone().getPhone()]))
        return len(result), result

    def searchByLastName(self, item):
        if not self.searchByTrieLastName(item):
            return 0, []
        contacts = self.contactService.contacts
        ids = list(self.contactService.contacts.keys())
        result = []
        for id in ids:
            contact = contacts[id]
            if self.search.searchInStringPrefix(item, contact.getLastName()):
                result.append(
                    ([contact.getId(), contact.getFirstName(), contact.getLastName(), contact.getPhone().getPhone()]))
        return len(result), result

    def searchByPhoneNumber(self, item):
        if not self.searchByTriePhoneNumber(item):
            return 0, []
        contacts = self.contactService.contacts
        ids = list(self.contactService.contacts.keys())
        result = []
        for id in ids:
            contact = contacts[id]
            if self.search.searchInStringPrefix(item, contact.getPhone().getPhone()):
                result.append(
                    ([contact.getId(), contact.getFirstName(), contact.getLastName(), contact.getPhone().getPhone()]))
        return len(result), result

    def searchByTrieFirstName(self, word):
        current = self.contactService.firstnameTrie
        for l in word:
            if l not in current:
                return False
            current = current[l]
        return True

    def searchByTrieLastName(self, word):
        current = self.contactService.lastnameTrie
        for l in word:
            if l not in current:
                return False
            current = current[l]
        return True

    def searchByTriePhoneNumber(self, word):
        current = self.contactService.phoneNumberTrie
        for l in word:
            if l not in current:
                return False
            current = current[l]
        return True
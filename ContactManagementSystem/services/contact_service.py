from services.contact_service_interface import ContactServiceInterface
from models.contact import Contact


class ContactService(ContactServiceInterface):
    # db data
    contacts = {}
    firstnameTrie = {}
    lastnameTrie = {}
    phoneNumberTrie = {}

    def insertFirstName(self, word):
        current = self.__class__.firstnameTrie
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#'] = 1

    def insertLastName(self, word):
        current = self.__class__.lastnameTrie
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#'] = 1

    def insertPhoneNumber(self, word):
        current = self.__class__.phoneNumberTrie
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#'] = 1

    def addNewContact(self, id, firstname, lastname, phone):
        contact = Contact()
        contact.setId(id)
        contact.setFirstName(firstname)
        contact.setLastName(lastname)
        contact.setPhone(phone)

        self.__class__.contacts[id] = contact
        self.insertPhoneNumber(phone.getPhone())
        self.insertFirstName(firstname)
        self.insertLastName(lastname)
        return contact

    def updateContact(self, id, firstname, lastname, phone):
        if id not in self.__class__.contacts:
            return "Error: contact id does not exist"
        contact = self.__class__.contacts[id]
        contact.setId(id)
        contact.setFirstName(firstname)
        contact.setLastName(lastname)
        contact.setPhone(phone)

        self.__class__.contacts[id] = contact
        return contact

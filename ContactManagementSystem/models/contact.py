class Contact(object):

    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.phone = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setFirstName(self, firstname):
        self.firstname = firstname

    def getFirstName(self):
        return self.firstname

    def setLastName(self, lastname):
        self.lastname = lastname

    def getLastName(self):
        return self.lastname

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

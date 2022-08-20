class Phone(object):

    def __init__(self):
        self.phone = None
        self.countrycode = None

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getCountryCode(self):
        return self.countrycode

    def setCountryCode(self, countrycode):
        self.countrycode = countrycode

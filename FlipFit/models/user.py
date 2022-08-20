class User(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.type = "Regular"
        self.bookings = [] # [{"weights": (1,2,)}, {}]

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setBookings(self, bookings):
        self.bookings = bookings

    def getBookings(self):
        return self.bookings

    def setType(self, type):
        self.bookings = type

    def getType(self):
        return self.type

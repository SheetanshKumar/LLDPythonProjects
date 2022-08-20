class Gym(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.members = []
        self.slots = {}


    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMembers(self, members):
        self.members = members

    def getMembers(self):
        return self.members

    def setSlots(self, slots):
        self.slots = slots

    def getSlots(self):
        return self.slots


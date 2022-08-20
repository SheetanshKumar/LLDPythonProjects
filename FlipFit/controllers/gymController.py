class GymController(object):
    def __init__(self, gymService):
        self.gymService = gymService

    def addGym(self, id, name, slots):
        return self.gymService.addGym(id, name, slots)

    def getSlots(self):
        return self.gymService.getSlots()


from services.gym_service_interface import GymServiceInterface
from models.gym import Gym


class GymService(GymServiceInterface):

    gymDetails = {}

    def addGym(self, id, name, slots, days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "sunday"]):
        gym = Gym()
        gym.setId(id)
        gym.setName(name)
        if name in self.__class__.gymDetails:
            gym = self.__class__.gymDetails[name]


        slots = gym.getSlots() | slots
        gym.setSlots(slots)
        # print(gym.getSlots())

        self.__class__.gymDetails[name] = gym
        return gym

    def getSlots(self):
        gyms = self.__class__.gymDetails

        slots = []
        for key in gyms.keys():
            gym = gyms[key]
            slots.append((key, gym.getSlots()))
        return slots


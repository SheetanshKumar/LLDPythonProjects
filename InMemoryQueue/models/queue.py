class Queue(object):
    # defining in memory list to store queue data
    queue = {}
    def __init__(self):
        self.size = 0

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    #
    def pushMessage(self, topic, payload):
        self.__class__.queue[topic].append(payload)
        self.size += 1

    def pushMessage(self, topic, payload):
        if topic in self.__class__.queue.keys():
            self.__class__.queue[topic].append(payload)
            self.size += 1
            return True
        else:
            return False

    def popMessage(self, topic):
        if len(self.__class__.queue[topic]) > 0:
            self.size -= 1
            return self.__class__.queue[topic].pop(-1)

        else:
            return None

    def subscribeTopic(self, topic):
        self.__class__.queue[topic] = []

    def unsubscribeTopic(self, topic):
        del self.__class__.queue[topic]


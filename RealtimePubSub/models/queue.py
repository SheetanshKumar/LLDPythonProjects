import RealtimePubSub.models.message
class Queue(object):

    def __init__(self):
        self.size = 0
        self.topics = set()
        self.queue = dict()

    def getSize(self):
        return self.size

    def getTopics(self):
        return self.topics

    def addTopic(self, topic):
        self.topics.add(topic)
        self.queue[topic] = []

    def deleteTopic(self, topic):
        self.topics.remove(topic)
        del self.queue[topic]

    def pushMessage(self, topic, payload):
        if topic not in self.getTopics():
            self.addTopic(topic)
        self.queue[topic].append(payload)

    def popMessage(self, topic):

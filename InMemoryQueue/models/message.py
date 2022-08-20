class Message(object):
    def __init__(self):
        self.topic = None
        self.payload = None
        self.retryCount = 10

    def getTopic(self):
        return self.topic

    def setTopic(self, topic):
        self.topic = topic

    def getPayload(self):
        return self.payload

    def setPayload(self, payload):
        self.payload = payload

    def getRetryCount(self):
        return self.retryCount

    def setRetryCount(self, retryCount):
        self.retryCount = retryCount

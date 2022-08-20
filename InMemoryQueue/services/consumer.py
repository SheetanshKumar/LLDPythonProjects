from models.queue import Queue


class Consumer(Queue):

    def __init__(self, queue):
        self.queue = queue

    def consumeMessage(self, topic):
        res = self.queue.popMessage(topic)
        if res != None:
            print("Message consumed: {}".format(res))
        return

    def subscribeTopic(self, topic):
        pass

    def unsubscribeTopic(self, topic):
        pass


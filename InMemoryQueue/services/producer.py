from models.queue import Queue
from services.consumer import Consumer
import json


class Validator(object):
    def __init__(self):
        pass

    def validateJSON(self, jsonData):
        try:
            json.loads(jsonData)
        except ValueError as err:
            return False
        return True


class Producer(Queue):

    def __init__(self):
        self.queue = Queue()
        self.consumer = Consumer(self.queue)

    # interface to produce, push
    def produceMessage(self, Message):
        validate = Validator()
        if validate.validateJSON(Message.getPayload()):
            res = self.queue.pushMessage(Message.getTopic(), Message.getPayload())
            if res == False:
                returnmsg = "Topic not subscribed, Message not added to the queue"
                print(returnmsg)
                return False
        else:
            returnmsg = "Message is not in JSON format, Message not added to the queue"
            print(returnmsg)
            return False

        returnmsg = "Message added to the queue"
        print(returnmsg)

        res = self.consumer.consumeMessage(Message.getTopic())

        return True

    def subscribeTopic(self, topic):
        self.queue.subscribeTopic(topic)

    def unsubscribeTopic(self, topic):
        self.queue.unsubscribeTopic(topic)

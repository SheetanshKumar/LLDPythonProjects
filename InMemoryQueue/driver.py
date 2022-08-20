__author__ = "Sheetansh Kumar"

import threading
import time

from models.queue import Queue
from models.message import Message
from services.producer import Producer

msg1 = Message()
msg1.setTopic("topic1")
msg1.setPayload('''{"id": 1, "item": "itemXyz"}''')

msg2 = Message()
msg2.setTopic("topic2")
msg2.setPayload("json2")

msg3 = Message()
msg3.setTopic("topic3")
msg3.setPayload('''{"id": 3, "item": "itemXyz"}''')

msg4 = Message()
msg4.setTopic("topic4")
msg4.setPayload("json4")

msg5 = Message()
msg5.setTopic("topic5")
msg5.setPayload("json5")

msgs = [msg1, msg2, msg3, msg4, msg5]

producer = Producer()


# This function handles mutithreading for producer and consumer
def asynchronousProducer(producer, message):
    producer.subscribeTopic(message.getTopic())
    producer.produceMessage(message)
    # added timer to check thread performance
    time.sleep(5)


def WithMultiThreading():
    for msg in msgs:
        t = threading.Thread(target=asynchronousProducer, args=(producer, msg,))
        t.start()


# This is synchronous queue -> FIFO
def WithoutMultiThreading():
    for msg in msgs:
        producer.subscribeTopic(msg.getTopic())
        producer.produceMessage(msg)


WithoutMultiThreading()

print('---------------------------\n')

# unsubscribing the topics from queue
for msg in msgs:
    producer.unsubscribeTopic(msg.getTopic())

# calling function to use threads
WithMultiThreading()

q = Queue()
print(q.queue)

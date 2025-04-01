__author__= "sheetansh"

# User -> name, id, email, phone
# Coin -> name, id, value, currentPrice, highPrice, volume, marketCap
# Notification -> id, Coin
# createNotification(Coin, )
# deleNotificationById(id)
# Subscription -> user, notification
#   subcribe(user, coin, mode)
#   unsubcribe

# MessageBus -> push, get()



# create -> messageQueue   ->  - - - -
from collections import defaultdict
class User:
    id = None
    name = str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def removeUser(self, id):
        pass


class Coin:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.currentPrice = price

    def deleteCoin(self, id):
        pass

class Notification:
    notifList = []

    def __init__(self, id, coin):
        self.id = id
        self.coin = coin


    def deleteNotification(self, id):
        pass

    def addNotification(self, notif):
        self.notifList.append(notif)


class Controller:

    def __init__(self):
        self.msgClient = MessageBus()
        self.subs = Subscription()

    def createNotification(self, id, coin):
        notif = Notification(id, coin)
        notif.addNotification(notif)
        self.msgClient.push(notif)
        print("Notification for coin %s is created".format(coin.name))

    def subscribe(self, user, coin):
        self.subs.subscribe(user, coin)

    def unsubscribe(self, user, coin):
        self.subs.unsubscribe(user, coin)


# this will use singleton pattern
class MessageBus:

    def __init__(self):
        self.q = defaultdict(list)
        self.qlist = []

    def push(self, notification):
        self.q[notification.coin].append(notification)
        self.qlist.append(notification)

    def pop(self):
        cur = self.qlist.pop()
        self.q[cur.coin].pop()
        return cur

    def popOnCoin(self, coin):
        cur = self.q[coin].pop()
        return cur

class Subscription:

    def __init__(self):
        # dictionary of coin -> [Users]
        self.subs = defaultdict(list)

    def subscribe(self, user, coin):
        self.subs[coin].append(user)
        print("subscription successful for %s and %s".format(user, coin))

    def unsubscribe(self, user, coin):
        self.subs[coin].remove(user)



user = User("id1", "sheetansh")
user2 = User("id2", "sheetansh2")
coin1 = Coin("coinid1", "Bitcoin1", "1234")
coin2 = Coin("coinid2", "Bitcoin2", "12345")
coin3 = Coin("coinid3", "Bitcoin3", "12346")
controller = Controller()
controller.subscribe(user.id, coin1.id)
controller.subscribe(user.id, coin2.id)
controller.subscribe(user2.id, coin2.id)
controller.subscribe(user2.id, coin3.id)
controller.createNotification("id1", coin1)


















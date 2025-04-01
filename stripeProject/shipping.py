'''
calculate the total shipping cost giving the discounted account
i.e if a user buys 5 shoes and shipping to US, the first 3 shoes will cost 5 each
and the remaining will cost 2 each.
use orders.json and cost.json
'''


from collections import defaultdict
import json
class Item:

    def __init__(self, name, cost, location, minQ, maxQ):
        self.name = name
        self.cost = cost
        self.location = location
        self.minQ = minQ
        self.maxQ = maxQ


class Items:
    def __init__(self):
        self.items = []

    def addItemObj(self, item):
        self.items.append(item)

    def addItem(self, name, cost, location, minQ, maxQ):
        self.items.append(Item(name, cost, location, minQ, maxQ))

    def getItemsByLocationAndName(self, location, name):
        res = []
        for item in self.items:
            if item.location == location and item.name == name:
                res.append(item)
        return res

    def getItemsByLocation(self, location):
        res = defaultdict(list)
        for item in self.items:
            if item.location == location :
                res[item.name].append(item)
        return res

    def getItemsByName(self, name):
        res = defaultdict(list)
        for item in self.items:
            if item.name == name:
                res[name].append(item)
        return res

class Parser:

    def __init__(self):
        pass

    def getItemObject(self, jsonString):
        py_obj = json.loads(jsonString)

    def getJsonObjFromFile(self, filename):
        with open(filename, "r") as file:
            pyObj = json.load(file)
            return pyObj

    def getItemObjListFromPyObj(self, pyObj):
        items = []
        for name in list(pyObj.keys()):
            for loc in list(pyObj[name].keys()):
                for priceMatrix in pyObj[name][loc]:
                    price = priceMatrix["price"]
                    minQ = priceMatrix["minQty"]
                    maxQ = priceMatrix["maxQty"]
                    items.append(Item(name, price, loc, minQ, maxQ))
        return items

    def parseAndSaveOrders(self, filename, OrdersClass):
        with open(filename, "r") as file:
            pyObj = json.load(file)
            for loc in list(pyObj.keys()):
                for item in pyObj[loc]["items"]:
                    quan = item["quantity"]
                    name = item["item"]
                    OrdersClass.addOrder(Order(loc, name, quan))

class Order:

    def __init__(self, loc, name, quantity):
        self.location = loc
        self.name = name
        self.quantity = quantity

class Orders:

    def __init__(self):
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)

    def calculateOrderCost(self, order, itemclass):
        items = itemclass.getItemsByLocationAndName(order.location, order.name)
        items.sort(key=lambda item: item.cost)

        cost = 0
        for item in items:
            if order.quantity < item.minQ:
                continue
            if item.maxQ == None or order.quantity <= item.maxQ:
                cost += order.quantity * item.cost
                return cost
            if order.quantity > item.maxQ:
                cost += item.cost*(item.maxQ)
                order.quantity -= item.maxQ
                # print(cost)
        return 0

    def calculateCost(self, itemclass):
        for order in self.orders:
            # print(order.name, order.location, order.quantity)
            cost = self.calculateOrderCost(order, itemclass)
            if cost == 0:
                print("Order can't be placed for order", order.name, order.location, order.quantity)
            else:
                print("cost for order: " + order.name + "= ", cost)


parser = Parser()

pyObj = parser.getJsonObjFromFile("cost.json")
items = parser.getItemObjListFromPyObj(pyObj)
itemClass = Items()
for item in items:
    itemClass.addItemObj(item)

itemByLoc = itemClass.getItemsByLocation("CA")
print(itemByLoc["cup"][1].cost)

OrderClass = Orders()
parser.parseAndSaveOrders("orders.json", OrderClass)
OrderClass.calculateCost(itemClass)


'''
Given an inputString: "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7" (etc) find the cost to ship an item from X to Y (ie: US to UK ==> Cost of 5).
From the previous solution, with the same inputString find the cost if you need to use an intermediate step. For instance US -> CA -> UK and it's associated cost.
'''
import copy
import heapq
from collections import defaultdict
from collections import deque
inputString = "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7:CA,IND,UPS,25"

class Order:

    def __init__(self, src, dest, mode, cost):
        self.src = src
        self.dest = dest
        self.mode = mode
        self.cost = cost


class Orders:

    def __init__(self):
        self.orders = []
        self.graph = defaultdict(list)

    def addOrder(self, order):
        self.orders.append(order)

    def getAllOrders(self):
        return self.orders

    def parseAndSaveOrders(self, inputString):
        orderstrlist = inputString.strip().split(":")
        for orderstr in orderstrlist:
            src, dest, mode, cost = orderstr.split(",")
            order = Order(src, dest, mode, int(cost))
            self.orders.append(order)
            self.graph[src].append((dest, int(cost)))

    def calculateEachCost(self):
        for order in self.orders:
            print(order.src, order.dest, order.cost, order.mode)

    def calculateSrcToDestCostAndPath(self, src, dest):

        heap = [(0, src, [])]
        vis = dict()

        while(len(heap) != 0):
            current, node, path = heapq.heappop(heap)
            if node in vis and vis[node] <= current:
                continue
            #      use deepcopy here to avoid list reference
            path = path + [node]
            vis[node] = current
            if node == dest:
                print("path=", path)
                return current, path

            for neigh, cost in self.graph[node]:
                if neigh not in vis or vis[neigh] > current+cost:
                    heapq.heappush(heap, (current+cost, neigh, path))
        return None, []

    def calculateIntermediateCost(self, src, inter, dest):
        pass


orders = Orders()
orders.parseAndSaveOrders(inputString)
orders.calculateEachCost()
cost, path = orders.calculateSrcToDestCostAndPath("US", "UK")
print(cost, path)

cost, path = orders.calculateSrcToDestCostAndPath("UK",  "CA")
print(cost, path)

cost, path = orders.calculateSrcToDestCostAndPath("US", "IND")
print(cost, path)

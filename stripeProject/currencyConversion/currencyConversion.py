'''
The interviewer explained that the problem would be divided into four parts, and
I would be evaluated based on completion and code quality.
Part 1: Parse a string in the format "USD:CAD:DHL:5,USD:GBP:FEDX:10",
representing currency conversion rates from a source to a target currency
and the associated shipping method. Write a method to convert a given amount from one currency to another.
Only direct conversions are allowed.

Part 2: Write a method that returns the cost and shipping methods involved, allowing at most one hop in the conversion from one currency to another.

Part 3: Write a method that returns the minimum cost and involved shipping methods, allowing at most one hop for the conversion.
'''

from collections import defaultdict

st = "USD:CAD:DHL:5,USD:GBP:FEDX:10,CAD:INR:FEDX:25,CAD:GBP:FEDX:1"

class CurrenyConversion:

    def __init__(self, cur, to, mode, amt):
        self.cur = cur
        self.to = to
        self.mode = mode
        self.amt = amt

class Currency:

    def __init__(self):
        self.curStore = []
        self.graph = defaultdict(dict)

    def parseAndAddCurrency(self, curStrings):
        curArr = curStrings.split(',')
        for curStr in curArr:
            if not curStr or curStr == "":
                continue
            try:
                cur, to, mode, amt = curStr.split(':')
                curObj = CurrenyConversion(cur, to, mode, int(amt))
                self.curStore.append(curObj)
                self.graph[cur][to] = (int(amt), mode)
            except:
                print('not able to unpack, wrong input')
                continue

    def converDirect(self, fromCur, toCur):
        for curObj in self.curStore:
            if curObj.cur == fromCur and curObj.to == toCur:
                return curObj.mode, curObj.amt, None
        return None, None, "Not possible"


    def convertByOneHop(self, fromCur, toCur):
        for curObj in self.curStore:
            if curObj.cur == fromCur and curObj.to == toCur:
                return curObj.mode, curObj.amt, None
            if curObj.cur == fromCur:
                mode, amt, err = self.converDirect(curObj.to, toCur)
                if not err:
                    totalamt = curObj.amt * amt
                    totalmode = [curObj.mode, mode]
                    return totalmode, totalamt, None
        return None, None, "Not possible"

    def calculateMinimumCostByAtMostOneHop(self, fromCur, toCur):
        res = []
        for curObj in self.curStore:
            if curObj.cur == fromCur and curObj.to == toCur:
                 res.append((curObj.amt, curObj.mode))
            mode, amt, err = self.converDirect(curObj.to, toCur)
            if not err:
                totalamt = curObj.amt * amt
                totalmode = [curObj.mode, mode]
                res.append((totalamt, totalmode))
        res.sort()
        print(res)
        return res[0]

    def converDirect1(self, fromCur, toCur):
        if toCur in self.graph[fromCur]:
            return self.graph[fromCur][toCur], None
        return None, "Not Possible"

    def convertByOneHop1(self, fromCur, toCur):
        res, err = self.converDirect1(fromCur, toCur)
        if not err:
            return res

        for key in self.graph[fromCur].keys():
            if toCur in self.graph[key]:
                totalamt = self.graph[fromCur][key][0] * self.graph[key][toCur][0]
                totalmode = [self.graph[fromCur][key][1],  self.graph[key][toCur][1]]
                return (totalamt, totalmode), None
        return None, "Not Possible"


    def print(self):
        print(self.curStore)
        print(self.graph)

curcon = Currency()
curcon.parseAndAddCurrency(st)
# curcon.print()
mode, amt, err = curcon.converDirect("USD", "CAD")
assert mode == "DHL"
assert amt == 5
assert err is None

mode, amt, err = curcon.converDirect("CAD", "USD")
assert mode is None
assert amt is None
assert err == "Not possible"


# part 2
mode, amt, err = curcon.convertByOneHop("USD", "INR")
print(mode, amt, err)

# part 3
mode, amt = curcon.calculateMinimumCostByAtMostOneHop("USD", "GBP")
print(mode, amt)

# part 1 by using dict

res, err = curcon.converDirect1("USD", "CAD")
print(res, err)

# part 2 by using dict
res, err = curcon.convertByOneHop1("USD", "INR")
print(res, err)
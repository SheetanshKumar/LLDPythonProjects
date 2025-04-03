'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

#     payment="paymentABC,500,Paying off: invoiceC", invoices=["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"]
#     f("payment5,1000,Paying off: invoiceC", ["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"])
#     payment5 pays off 1000 for invoiceC due on 2023-01-30
'''
import datetime
# date1 = datetime.datetime.strptime("2015-01-30", "%Y-%m-%d")
inputpayment = "payment5,1000,Paying off: invoiceC"
invId =  ["invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000"]
class Payment:

    def __init__(self, payId, amt, invId):
        self.payId = payId
        self.amt = amt
        self.invId = invId


class Invoice:

    def __init__(self, invId, date, amt):
        self.invId = invId
        self.date = date
        self.amt = amt


class Store:

    def __init__(self):
        self.payStore = []
        self.invStore = {}
        self.invList = []

    def parseAndAddPayment(self, payString):
        payArr = payString.split(",")

        payId, amt, payingoff = payArr[0], payArr[1], payArr[2]
        invId = ""
        if len(payingoff.split(":")) == 2:
            invId = payingoff.split(":")[1]
        invId = invId.strip()
        payObj = Payment(payId, int(amt), invId)
        print(payObj.invId)
        self.payStore.append(payObj)


    def parseAndAddInvoice(self, invList):
        for invString in invList:
            invId, date, amt = invString.split(",")
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            invObj = Invoice(invId, date, int(amt))
            self.invStore[invId] = invObj
            self.invList.append(invObj)


    def AcknowledgePaymentInvoice(self, paymentString, invList):
        self.parseAndAddPayment(paymentString)
        self.parseAndAddInvoice(invList)

        payObj = self.payStore[0]
        if payObj.invId == "":
            totalInvs = []
            for invObj in self.invList:
                print(invObj.invId)
                if payObj.amt == invObj.amt:
                    totalInvs.append((invObj.date, invObj.invId, invObj.amt, payObj.payId))

            totalInvs.sort()
            resObj = totalInvs[0]

            return resObj[3]+ " pays off " +  str(resObj[2]) + " for " +  resObj[1]  +" due on " + str(resObj[0])
        elif payObj.invId in self.invStore:
            key = payObj.invId
            date = str(self.invStore[key].date).split()[0]
            return payObj.payId + " pays off " + str(payObj.amt) + " for " + payObj.invId +" due on " + date
        return "payment not possible"


storeObj = Store()
# print(storeObj.AcknowledgePaymentInvoice(inputpayment, invId))

payStr = "paymentUUID,500,Bank transfer"
invoiceList = ["invoiceA,2024-02-01,500", "invoiceB,2024-01-01,500"]

expectedOutput = 'paymentUUID pays off 500 for invoiceB due on 2024-01-01'

print(storeObj.AcknowledgePaymentInvoice(payStr, invoiceList))
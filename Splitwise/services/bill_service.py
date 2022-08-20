from services.bill_service_interface import BillServiceInterface
from models.bill import Bill


class BillService(BillServiceInterface):
    # adding class level dictionary to set it in the db, here it is in-memory
    billDetails = {}

    def addBill(self, id, groupId, amount, contribution, paidBy):
        bill = Bill()
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill
        return bill

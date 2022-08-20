import sys
# sys.path.append()
from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.bill_service import BillService
from services.user_service import UserService
from services.group_service import GroupService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('1', 'sheetansh')
user2 = userController.addUser('2', 'monu')
user3 = userController.addUser('3', 'dumpy')
user4 = userController.addUser('4', 'papa')
user5 = userController.addUser('5', 'mummy')

members = [user1, user2, user3, user4, user5]
group1 = groupController.addGroup('group1', 'family', members)

# print(group1.getMembers())

paidBy = {'1':200, '2': 100, '3': 50, '4':50, '5': 100}
contribution = {'1':100, '2': 100, '3': 100, '4':100, '5': 100}

bill1 = billController.addBill('bill1', 'group1', 500, contribution, paidBy)

balance = billController.getUserBalance('1')
print(balance)

__author__ = "sheetansh"
__email__ = "sheetansh123@gmail.com"

from controllers.contact_controller import ContactController
from services.contact_service import ContactService


contactController = ContactController(ContactService())

con1 = contactController.addNewContact('1', "Sheetansh", "Kumar", "+123467890")
con2 = contactController.addNewContact('2', "Rahul", "Gupta", "+467890")
con3 = contactController.addNewContact('3', "Ramesh", "Singh", "+7890")
con4 = contactController.addNewContact('4', "Harsh", "Singh", "+7890")
con5 = contactController.addNewContact('5', "Dev", "Raj", "+7890")

#  search by firstname
print(contactController.searchByType("Shee", "firstname"))
print(contactController.searchByType("Ra", "firstname"))
print()

# search by lastname
print(contactController.searchByType("Si", "lastname"))
print()

# search by phone
print(contactController.searchByType("+", "phonenumber"))
print()

# update contact
contactController.updateContact('2', "Ram", "Gupta", "+1234")
print(contactController.searchByType("Ra", "firstname"))
print(contactController.searchByType("Dev", "firstname"))
print()

# update contact
contactController.updateContact('5', "Devender", "D", "+1234")
print(contactController.searchByType("Dev", "firstname"))
print()

# no contacts
print(contactController.searchByType("**", "firstname"))
print()

# return all contacts from search
print(contactController.searchByType("", "firstname"))


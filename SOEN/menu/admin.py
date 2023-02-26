from boilerplate.inputs import getIntegerInRange
from entity.Message import *
from entity.User import *
def adminMainMenu():
    admin = Admin.getAdmin()
    choice = getIntegerInRange("1.Show all messages",1,1)
    if choice == 1:
        showAllNotifications(admin.username)
    
def showComplaints(adminID):
    showAllNotifications(adminID)

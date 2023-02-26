import datetime
from entity.data import *



def broadcastNotification(sender, message):
    for user in users:
        if user != sender:
            sendPrivateNotification(
                sender=sender, reciever=user["username"], message=message)


def sendPrivateNotification(sender, reciever, message):
    newNotification = {"sender": sender, "message": message,
                       "timeStamp": datetime.datetime.now()}
    if reciever in notifications.keys():
        notifications[reciever].append(
            {"sender": sender, "message": message, "timeStamp": datetime.datetime.now()})
    else:
        notifications[reciever] = [newNotification]


def showAllNotifications(username):
    if username in notifications.keys():
        for notification in notifications[username]:
            messageSize = 70
            isComplaint = False
            rawMessage = ""
            if "COMPLAINT:" in notification["message"]:
                isComplaint = True
                rawMessage = notification["message"].replace("COMPLAINT:","")
            else:
                rawMessage = notification["message"]
            if len(notification["message"]) > 60:
                messageSize = len(notification["message"]) + 40
            print("-"*messageSize)
            print("|{label:<34}|{value:>34}|".format(
                label="Type", value= "Message" if not isComplaint else "Complaint"))
            print("|{label:<34}|{value:>34}|".format(
                label="Sender", value=notification["sender"]))
            print("|{label:<34}|{value:>34}|".format(
                label="Message", value=rawMessage))
            print("|{label:<34}|{value:>34}|".format(
                label="TIme", value=notification["timeStamp"].strftime('%c')))
            print("-"*messageSize)


def sendComplaint(sender, message):
    for user in users:
        if user["userType"] == ADMIN:
            sendPrivateNotification(
                sender=sender, reciever=user["username"], message="COMPLAINT:" + message)

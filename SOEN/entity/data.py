
from boilerplate.contants import *
notifications = {}
users = [{
    "username": "owner",
    "password": "owner",
    "userType": OWNER
}, {
    "username": "customer1",
    "password": "customer1",
    "userType": CUSTOMER
}, {
    "username": "customer2",
    "password": "customer2",
    "userType": CUSTOMER
}, {
    "username": "admin",
    "password": "admin",
    "userType": ADMIN
}]
categories = {
    CINEMA: {}, RESTAURANT: {}, AIRPLANE: {}, CONFIERENCE: {}, HOTEL: {}
}
sellList = {
    CINEMA: {}, RESTAURANT: {}, AIRPLANE: {}, CONFIERENCE: {}, HOTEL: {}
}
exchangeTicketList = {
    CINEMA: {}, RESTAURANT: {}, AIRPLANE: {}, CONFIERENCE: {}, HOTEL: {}
}

from menu.owner import *
from menu.customer import *
from menu.admin import *
from entity.User import *
if __name__ == "__main__":
    while (True):
        choice = getIntegerInRange(
            "Choose User Type:\n1.Admin\n2.Owner\n3.Customer\n4.Exit", 1, 4)
        if choice == 1:
            adminMainMenu()
        elif choice == 2:
            ownerMainMenu()
        elif choice == 3:
            customerMainMenu()
        else:
            break

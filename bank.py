from account import *


class Bank(object):
    """Driver class that runs the entire program."""

    def __init__(self):
        self.lower_limit = 1000
        self.user_choice = 0
        self.account_name = ""
        self.account_id = 0
        self.deposit_amount = 0
        self.account_balance = 1000
        self.withdraw_amount = 0
        self.account_pin = 0
        self.account_pin_confirm = 0
        self.menu_msg = ""
        self.object_name = None

    def show_main_menu(self):
        self.menu_msg = "\nPlease select an action " + "\n1---Withdraw" + "\n2---Deposit" + "\n3---Check balance" + \
                        "\n4---Log out" + "\n5---Exit"
        print(self.menu_msg)
        self.user_choice = int(input())
        if self.user_choice == 1:
            self.object_name.withdraw()
        elif self.user_choice == 2:
            self.object_name.deposit()
        elif self.user_choice == 3:
            print("Your current account balance is: ", self.object_name.account_balance)
        elif self.user_choice == 4:
            self.object_name.log_in_menu()
        elif self.user_choice == 5:
            print("Quitting... ")
            quit()
        else:
            # TODO Handle errors for non-int inputs maybe in unit tests
            print("Invalid choice. Please try again: ")
        self.show_main_menu()


# Objects for debugging purposes only
a = Bank()

b = Account()
b.deposit()
print(a.show_main_menu())
print(b.log_in_menu())
a.show_main_menu()

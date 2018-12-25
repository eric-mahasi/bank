import account
import sys
# TODO choose proper names for objects and some variables such as object_name to remove errors in evaluate_user_choice


def initialize_objects():
    global eric, victor, test
    eric = account.Account("eric", 1, 10000, 54, 256, 50)
    victor = account.Account("victor", 2, 3500, 8493, 2097, 672)
    test = account.Account("test", 3, 15688, 65984, 245788, 1000)


class Bank(object):
    """Driver class that runs the entire program."""
# TODO figure out variables to be instantiated in init function, if any necessary
    def __init__(self):
        self.user_choice = 0
        pass

    def display_welcome_msg(self):
        msg = 'Welcome user!\n' + '\nPlease select an action ' + \
              '\n1---Withdraw' + '\n2---Deposit' + '\n3---Check balance' + \
              '\n4---Exit'
        return msg

    # TODO add functionality:
    # 1) Modify objects to allow parameter values to be input by user such that each user creates a different object;
    # account creation
    # 2) Allow different users to access their own different accounts; login verification
    # 3) Enhance navigation through menus
    def nav_menu(self):
        """Allows users to navigate through the several menus"""
        print("Do you have an account? ")

    def get_user_choice(self):
        self.user_choice = int(input())

# FIXME unresolved attributes
    def evaluate_user_choice(self, user_choice):
        if user_choice == 1:
            self.withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
            self.withdraw(self.withdraw_amount)
        elif user_choice == 2:
            self.deposit_amount = int(input("Please enter the amount you wish to deposit: "))
            self.deposit(self.deposit_amount)
        elif user_choice == 3:
            print("You current account balance is: ", self.display_balance())
        elif user_choice == 4:
            print("Quitting... ")
            sys.exit()
        else:
            # TODO Handle errors for non-int inputs
            print("Invalid choice. Please try again: ")


# Objects for debugging purposes only
a = Bank()
a.display_welcome_msg()
a.get_user_choice()
a.evaluate_user_choice(a.user_choice)

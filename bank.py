import account
import sys


class Bank(object):
    """Driver class that runs the entire program."""
    def __init__(self):
        self.user_choice = 0
        self.account_name = ""
        self.account_id = 0
        self.deposit_amount = 0
        self.account_balance = 0
        self.withdraw_amount = 0
        self.withdraw_limit = 0
        self.msg = ""
        self.object_name = account.Account(self.account_name, self.account_id, self.account_balance,
                                           self.deposit_amount, self.withdraw_amount, self.withdraw_limit)

    def display_welcome_msg(self):  # TODO rename this function to something more suiting
        self.msg = "\nPlease select an action " + "\n1---Withdraw" + "\n2---Deposit" + "\n3---Check balance" + \
                   "\n4---Exit"
        print(self.msg)

    # TODO add functionality:
    # 1) Allow different users to access their own different accounts
    # 2) Enhance navigation through menus
    def nav_menu(self):
        """Allows users to navigate through the several menus."""
        print("Welcome user... ")
        n = input("Do you have an account? Y/N ")  # TODO choose more descriptive variable name
        if n.lower() == "y":
            self.verify_login()
        elif n.lower() == "n":
            print("Please be patient while we set up an account for you... ")
            self.create_account()
            print("\nAccount creation successful. Welcome " + str(self.object_name.account_name.title()) + "\n")
        else:
            print("Invalid choice. Please try again")

# TODO provide much more informative print statements; clarify output
    def create_account(self):
        """Create an account, passing user input into the parameters for Account objects. Returns an Account object."""
        self.account_name = input("Account name: ")
        self.account_id = int(input("Account ID: "))
        self.account_balance = int(input("Account balance: "))
        self.object_name = account.Account(self.account_name, self.account_id, self.account_balance,
                                           self.deposit_amount, self.withdraw_amount, self.withdraw_limit)
        return self.object_name

    def verify_login(self):
        """Check if account name and account id provided by user match those stored in file."""
        # TODO improve security by adding password functionality to user accounts
        pass

    def get_user_choice(self):  # FIXME probably no point in this being a function
        self.user_choice = int(input())

    def evaluate_user_choice(self, user_choice):
        if user_choice == 1:
            self.withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
            self.object_name.withdraw(self.withdraw_amount)
        elif user_choice == 2:
            self.deposit_amount = int(input("Please enter the amount you wish to deposit: "))
            self.object_name.deposit(self.deposit_amount)
        elif user_choice == 3:
            print("You current account balance is: ", self.object_name.display_balance())
        elif user_choice == 4:
            print("Quitting... ")
            sys.exit()
        else:
            # TODO Handle errors for non-int inputs
            print("Invalid choice. Please try again: ")


# Objects for debugging purposes only
a = Bank()
a.nav_menu()
a.display_welcome_msg()
a.get_user_choice()
a.evaluate_user_choice(a.user_choice)

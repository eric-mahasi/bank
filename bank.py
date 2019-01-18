import account
import sys


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
        self.object_name = account.Account(self.account_name, self.account_id, self.account_balance,
                                           self.deposit_amount, self.withdraw_amount)

    def show_main_menu(self):
        self.menu_msg = "\nPlease select an action " + "\n1---Withdraw" + "\n2---Deposit" + "\n3---Check balance" + \
                        "\n4---Exit"
        print(self.menu_msg)

    # TODO add functionality:
    # 1) Allow different users to access their own different accounts
    # 2) Enhance navigation through menus. Make it possible for users to fluidly move through all the different menu
    # screens
    def navigate_menu(self):
        """Allows users to navigate through the several menus."""
        print("Welcome user... ")
        self.user_choice = input("Do you have an account? Y/N ")
        if self.user_choice.lower() == "y":
            self.verify_login()
        elif self.user_choice.lower() == "n":
            self.create_account()
        else:
            print("Invalid choice. Please try again.")
            self.navigate_menu()

    def create_account(self):
        """Create an account, passing user input into the parameters for Account objects. Returns an Account object."""
        print("Please be patient while we set up an account for you... ")
        print("\nKindly enter the appropriate information after each prompt below. ")
        self.account_name = input("Account name: ")
        # self.account_id = int(input("Account ID: "))  # TODO generate account ID sequentially from already existing
        # accounts
        while True:
            self.account_balance = int(input("Initial deposit amount: "))
            if self.account_balance <= self.lower_limit:
                print("Account balances lower than", self.lower_limit, "are not allowed. Please try again.")
            else:
                break
        # FIXME PIN functionality works for only one iteration instead of continually till the required conditions
        # are met
        # TODO make confirm pin into a method of it's own
        while True:
            self.account_pin = input("Account PIN: ")
            if len(self.account_pin) < 4:
                print("PIN must be at least four digits.")
            else:
                while True:
                    self.account_pin_confirm = input("Please enter PIN again: ")
                    if self.account_pin == self.account_pin_confirm:
                        print("PIN successfully recorded.")
                    else:
                        print("PINs do not match. Please try again.")
                        break
            break
        self.object_name = account.Account(self.account_name, self.account_id, self.account_balance,
                                           self.deposit_amount, self.withdraw_amount)
        print("\nAccount creation successful. Welcome " + str(self.object_name.account_name.title()) + ".")
        return self.object_name

    def verify_login(self):
        """Check if account name and account id provided by user match those stored in file."""
        print("Please be patient while we verify your details...")
        print("\nKindly enter the appropriate values after each prompt below. ")
        self.account_name = input("Account name: ")
        self.account_id = input("Account ID: ")
        self.account_pin = input("Account PIN: ")
        # TODO compare these values with those stored in the file
        # TODO figure out how to handle storing and accessing user account details in the file

    def get_user_choice(self):
        self.user_choice = int(input())

    def evaluate_user_choice(self):
        if self.user_choice == 1:
            self.withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
            if self.withdraw_amount >= self.lower_limit:
                print("Prohibited transaction. Withdrawal amount exceeded.")
            else:
                self.object_name.withdraw(self.withdraw_amount)
        elif self.user_choice == 2:
            self.deposit_amount = int(input("Please enter the amount you wish to deposit: "))
            self.object_name.deposit(self.deposit_amount)
        elif self.user_choice == 3:
            print("You current account balance is: ", self.object_name.display_balance())
        elif self.user_choice == 4:
            print("Quitting... ")
            sys.exit()
        else:
            # TODO Handle errors for non-int inputs maybe in unit tests
            print("Invalid choice. Please try again: ")


# Objects for debugging purposes only
a = Bank()
a.navigate_menu()
a.show_main_menu()
a.get_user_choice()
a.evaluate_user_choice()

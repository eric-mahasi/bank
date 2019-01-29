import account
import sys


class Bank(object):
    """Driver class that runs the entire program."""

    def __init__(self):
        self.lower_limit = 1000
        self.user_choice = 0
        self.account_pin = 0
        self.account_pin_confirm = 0
        self.menu_msg = ""

    def show_main_menu(self):
        self.menu_msg = ("\nPlease select an action "
                         "\n1---Withdraw"
                         "\n2---Deposit"
                         "\n3---Check balance"
                         "\n4---Log out"
                         "\n5---Exit")
        print(self.menu_msg)
        self.user_choice = int(input())
        if self.user_choice == 1:
            self.object_name.withdraw()
        elif self.user_choice == 2:
            self.object_name.deposit()
        elif self.user_choice == 3:
            print("Your current account balance is: ",
                  self.object_name.account_balance)
        elif self.user_choice == 4:
            self.log_in_menu()
        elif self.user_choice == 5:
            print("Quitting... ")
            sys.exit()
        else:
            # TODO Handle errors for non-int inputs maybe in unit tests
            print("Invalid choice. Please try again: ")
        self.show_main_menu()

    # TODO add functionality:
    # 1) Allow different users to access their own different accounts
    # TODO move all the following methods to account class
    def log_in_menu(self):
        """Allows users to navigate through the several menus."""
        print("Welcome...")
        print("\nPlease select an action " +
              "\n1---Log into my account" + "\n2---Create new account")
        self.user_choice = int(input())
        if self.user_choice == 1:
            self.verify_login()
        elif self.user_choice == 2:
            self.create_account()
        else:
            print("Invalid choice. Please try again.")
            self.log_in_menu()

    def create_account(self):
        """
        Create an account, passing user input into the parameters for
        Account objects.

        Returns an Account object.
        """
        print("Please be patient while we set up an account for you... ")
        print("\nKindly enter the appropriate information after each prompt"
              " below. ")
        self.account_name = input("Account name: ")

        # TODO generate account ID sequentially from already existing accounts
        # self.account_id = int(input("Account ID: "))

        while True:
            self.account_balance = int(input("Initial deposit amount: "))
            if self.account_balance <= self.lower_limit:
                print("Account balances lower than", self.lower_limit,
                      "are not allowed. Please try again.")
            else:
                break
        self.confirm_pin()
        self.object_name = account.Account(
            self.account_name, self.account_id, self.account_balance,
            self.deposit_amount, self.withdraw_amount)
        print("\nAccount creation successful. Welcome " +
              str(self.object_name.account_name.title()) + ".")
        return self.object_name

    # FIXME PIN functionality works for only one iteration instead of
    # continually till the required conditions are met
    def confirm_pin(self):
        """
        Handles a 4-digit number that will be used as a PIN for accessing user
        accounts. Ensures that the PIN is entered correctly by having the user
        enter it twice and the two entries are then compared to each other.

        Returns PIN.
        """
        while True:
            self.account_pin = input("Account PIN: ")
            # FIXME these if loops runs infinitely
            if len(str(self.account_pin)) < 4:
                print("PIN must be at least four digits.")
                break
            else:
                self.account_pin_confirm = input("Please enter PIN again: ")
                while True:
                    if self.account_pin == self.account_pin_confirm:
                        print("PIN successfully recorded.")
                    else:
                        print("PINs do not match. Please try again.")
                        break
                break
        return self.account_pin

    def verify_login(self):
        """
        Check if account name and account id provided by user match those
        stored in file.
        """
        print("Please be patient while we verify your details...")
        print("\nKindly enter the appropriate values after each prompt below.")
        self.account_name = input("Account name: ")
        self.account_id = input("Account ID: ")
        self.account_pin = input("Account PIN: ")
        # self.confirm_pin()
        # TODO compare these values with those stored in the file
        # TODO figure out how to handle storing and accessing user account
        # details in the file


# Objects for debugging purposes only
a = Bank()
a.log_in_menu()
a.show_main_menu()

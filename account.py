class Account(object):
    """This class handles all the basic operations of a rudimentary bank account."""

    def __init__(self):
        self.user_choice = int(input())
        self.lower_limit = 1000
        self.account_name = ""
        self.account_id = 0
        self.account_balance = 1000
        self.deposit_amount = 0
        self.withdraw_amount = 0
        self.account_pin = 0
        self.confirm_account_pin = 0
        self.object_name = None

    # FIXME bug in this method prevents withdrawal
    # FIXME account balance takes the value of 0

    def withdraw(self):
        self.withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
        if self.withdraw_amount >= self.account_balance:
            print("Prohibited transaction. Account balances lower than", self.lower_limit, "are not allowed. Please"
                                                                                           " try again.")
        else:
            # TODO prevent account balances lower than lower limit
            self.account_balance -= self.withdraw_amount
            print("Transaction successful. Your new account balance is", self.account_balance)

    def deposit(self):
        self.deposit_amount = int(input("Please enter the amount you wish to deposit: "))
        self.account_balance += self.deposit_amount
        print("Transaction successful. Your new account balance is", self.account_balance)

    def log_in_menu(self):
        """Allows users to navigate through the several menus."""
        print("Welcome...")
        print("\nPlease select an action " + "\n1---Log into my account" + "\n2---Create new account")
        if self.user_choice == 1:
            self.verify_login()
        elif self.user_choice == 2:
            self.create_account()
        else:
            print("Invalid choice. Please try again.")
            self.log_in_menu()

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
        self.confirm_pin()
        self.object_name = Account(self.account_name, self.account_id, self.account_balance,
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
        # self.confirm_pin()
        # TODO compare these values with those stored in the file
        # TODO figure out how to handle storing and accessing user account details in the file

        # FIXME PIN functionality works for only one iteration instead of continually till the required conditions
        # are met

    def confirm_pin(self):
        """Handles a 4-digit number that will be used as a PIN for accessing user accounts. Ensures that the PIN is
         entered correctly by having the user enter it twice and the two entries are then compared to each other.
         Returns PIN."""
        while True:
            self.account_pin = input("Account PIN: ")
            # FIXME these if loops runs infinitely
            if len(str(self.account_pin)) < 4:
                print("PIN must be at least four digits.")
                break
            else:
                self.confirm_account_pin = input("Please enter PIN again: ")
                while True:
                    if self.account_pin == self.confirm_account_pin:
                        print("PIN successfully recorded.")
                    else:
                        print("PINs do not match. Please try again.")
                        break
                break
        return self.account_pin

    # TODO add functionality:
    # 1) Allow different users to access their own different accounts

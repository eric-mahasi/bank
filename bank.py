import csv
import random
import sys

import account
import records


class Bank(object):
    """A class that simulates an ATM interface.

    This class provides the user with a text-based user interface that
    allows them to interact with their accounts and perform transactions
    on them. This class also implements certain features which provide
    extended functionality for user accounts.

    ...

    Attributes
    ----------

    Methods
    -------
    show_main_menu
        Displays the menu that allows users to perform transactions.
    log_in_menu
        Displays the menu that enables users to log into their accounts.
    create_account
        Opens a new account.
    get_pin
        Generates the account pin.
    verify_login
        Enables registered users to log into their accounts.
    quit
        Exits the program.
    """

    def show_main_menu(self):
        """Displays the menu that allows users to select which
        transactions they'd like to perform."""
        while True:
            menu_msg = ("\nPlease select an action "
                        "\n1---Withdraw"
                        "\n2---Deposit"
                        "\n3---Check balance"
                        "\n4---Log out"
                        "\n5---Exit")
            print(menu_msg)

            choices = {'1': self.user_account.withdraw,
                       '2': self.user_account.deposit,
                       '3': self.user_account.print_account_balance,
                       '4': self.log_in_menu,
                       '5': self.quit}

            user_choice = choices.get(input())
            if user_choice is not None:
                user_choice()
            else:
                # TODO Handle errors for non-int inputs maybe in unit tests
                print("Invalid choice. Please try again: ")

    # TODO add functionality: Allow different users to access their own
    # different accounts
    def log_in_menu(self):
        """Displays the menu that allows registered users to log into their
        accounts and new users to create accounts."""
        while True:
            print("Welcome...")
            print("\nPlease select an action "
                  "\n1---Log into my account"
                  "\n2---Create new account")

            choices = {'1': self.verify_login,
                       '2': self.create_account}
            user_choice = choices.get(input())

            if user_choice is not None:
                user_choice()
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        """Opens a new account.

        The user provides details which are used to create a new account are
        then stored
        """
        print("Please be patient while we set up an account for you... ")
        print("\nKindly enter the appropriate information after each prompt"
              " below. ")
        account_name = input("Account name: ")

        # TODO: Generate account ID sequentially from already existing accounts
        # Temporary account id generation
        # Generates random 6 digit integer
        account_id = round(random.uniform(100_000, 999_999))

        while True:
            account_balance = int(input("Initial deposit amount: "))

            lower_limit = account.Account.LOWER_LIMIT
            if account_balance <= lower_limit:
                print("Account balances lower than", lower_limit,
                      "are not allowed. Please try again.")
            else:
                break

        account_pin = self.get_pin()

        self.user_account = account.Account(
            account_name, account_id, account_pin, account_balance)
        print("\nAccount creation successful. Welcome " +
              str(self.user_account.account_name.title()) + ".")
        account_details = {'name': self.user_account.account_name,
                           'id': self.user_account.account_id,
                           'pin': self.user_account.account_pin,
                           'balance': self.user_account.account_balance}

        self.record = records.Record()
        self.record.write_to_file(account_details)

    def get_pin(self):
        """Enables new users to enter a four digit PIN.

        This pin will then be used to access the user account on
        subsequent log ins.

        Returns
        -------
        account_pin : int
            The account PIN.

        """

        while True:
            account_pin = input("Account PIN: ")
            if len(str(account_pin)) < 4:
                print("PIN must be at least four digits.")
                continue
            else:
                account_pin_confirm = input("Please enter PIN again: ")

                if account_pin == account_pin_confirm:
                    print("PIN successfully recorded.")
                    break
                else:
                    print("PINs do not match. Please try again.")

        return account_pin

    def verify_login(self):
        """Enables registered users to access their accounts.

        The details provided by users on log in are compared against
        the details stored in the file.
        """

        print("Please be patient while we verify your details...")
        print("\nKindly enter the appropriate values after each prompt below.")

        file_name = "records.csv"

        # Opening the first before the start of the while loop to have it in
        # memory so as to prevent opening and closing of the file in case of
        # incorrect details.
        with open(file_name) as record_file:
            verified = False
            while not verified:
                account_name = input("Account name: ")
                account_pin = input("Account PIN: ")

                # Changing the stream position to the start of the file
                record_file.seek(0)
                record_reader = csv.reader(record_file, delimiter=',')
                for row in record_reader:
                    if account_name == row[0] and account_pin == row[2]:
                        print("Successfully logged in. Welcome",
                              account_name.title(), ".")
                        self.user_account = account.Account(
                            row[0], row[1], row[2], row[3])

                        verified = True
                        break

                if not verified:
                    print("Incorrect details entered. Try again.")

    def quit(self):
        """Exit the program."""
        print("Quitting... ")
        sys.exit()


# Objects for debugging purposes only
a = Bank()
a.log_in_menu()
a.show_main_menu()

import account
import sys

import random


class Bank(object):
    """Driver class that runs the entire program."""

    def show_main_menu(self):
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

    # TODO add functionality:
    # 1) Allow different users to access their own different accounts
    # TODO move all the following methods to account class
    def log_in_menu(self):
        """Allows users to navigate through the several menus."""
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
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        """
        Create an account, passing user input into the parameters for
        Account objects.
        """
        print("Please be patient while we set up an account for you... ")
        print("\nKindly enter the appropriate information after each prompt"
              " below. ")
        account_name = input("Account name: ")

        # TODO generate account ID sequentially from already existing accounts
        # self.account_id = int(input("Account ID: "))

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

    def get_pin(self):
        """
        Handles a 4-digit number that will be used as a PIN for accessing user
        accounts. Ensures that the PIN is entered correctly by having the user
        enter it twice and the two entries are then compared to each other.

        Returns PIN.
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
        """
        Check if account name and account id provided by user match those
        stored in file.
        """
        print("Please be patient while we verify your details...")
        print("\nKindly enter the appropriate values after each prompt below.")
        account_name = input("Account name: ")
        account_id = input("Account ID: ")
        account_pin = input("Account PIN: ")
        # self.get_pin()
        # TODO compare these values with those stored in the file
        # TODO figure out how to handle storing and accessing user account
        # details in the file

    def quit(self):
        print("Quitting... ")
        sys.exit()


# Objects for debugging purposes only
a = Bank()
a.log_in_menu()
a.show_main_menu()

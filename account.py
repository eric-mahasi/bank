import csv

import pandas as pd


class Account(object):
    """A class that performs the basic functionality associated with a
    bank account.

    ...

    Attributes
    ----------
    LOWER_LIMIT : int
        an arbitrary figure for the least amount of money an account is
        allowed to have.
    account_name : str
        the name associated with an account.
    account_id : int
        a single number that uniquely identifies each account.
    account_pin : int
        a four digit integer used to access user accounts.
    account_balance : int
        the amount of money currently in the account.

    Methods
    -------
    withdraw
        Withdraws money from the account.
    deposit
        Deposits money into the account.
    print_account_balance
        Displays the amount of money currently in the account.
    update_balance
        Changes the value of the account balance stored in the file.
    update_file
        Changes the values of stored user account details.
    """

    LOWER_LIMIT = 1000

    def __init__(
            self, account_name, account_id, account_pin, account_balance=1000):
        """
        Parameters
        ----------
        account_name : str
            The name associated with an account.
        account_id : int
            A six digit integer used to uniquely identify user accounts.
        account_pin : int
            A six digit integer used to uniquely identify user accounts.
        account_balance : int
            The amount of money currently in the account.
        """

        self.file_name = "records.csv"
        self.account_name = account_name
        self.account_id = account_id
        self.account_pin = account_pin
        self.account_balance = int(account_balance)
        self.transaction_prompt = str("Transaction successful. Your new "
                                      "account balance is:")

    def withdraw(self):
        """Withdraws money from the account.

        The amount of money that the user wishes to withdraw from the
        account is deducted from the current account balance.
        """

        prompt = "Please enter the amount you wish to withdraw: "
        withdraw_amount = int(input(prompt))
        if withdraw_amount > self.account_balance:
            print(
                "Prohibited transaction. Withdrawals in excess of the "
                "account balance are not allowed. Please try again.")
        else:
            self.account_balance -= withdraw_amount
            if self.account_balance < self.LOWER_LIMIT:
                print(
                    "Prohibited transaction. Account balances lower than "
                    f"{self.LOWER_LIMIT} are not allowed. Please try again.")
                self.account_balance += withdraw_amount
            else:
                print(self.transaction_prompt, self.account_balance)
        self.update_balance(self.account_balance)

    def deposit(self):
        """Deposits money into the account.

        The amount of money that the user wishes to deposit into the
        account is added to the current account balance.
        """
        prompt = "Please enter the amount you wish to deposit: "
        deposit_amount = int(input(prompt))

        self.account_balance += deposit_amount
        print(self.transaction_prompt, self.account_balance)
        self.update_balance(self.account_balance)

    def print_account_balance(self):
        """Displays the amount of money currently in the account."""
        print("Your current account balance is: " f"{self.account_balance}")

    def update_file(self, data, index):
        """Changes the values of stored user account details.

        Overwrite the currently stored user account details with new and
        up to date information.

        Parameters
        ----------
        data : int, str
            The new information that will be written to the file.
        index : int
            The row position in the file, representing which account
            detail will be changed.
        """
        with open(self.file_name) as record_file:
            # Read the entire file and store each line in a list
            record_reader = csv.reader(record_file, delimiter=',')
            lines = list(record_reader)
            # The value located at a specified position is assigned the
            # new data
            lines[int(self.account_id) - 1][index] = data
            df = pd.DataFrame(lines)
            # Removing the top row on the dataframe
            df.columns = df.iloc[0]
            df = df.reindex(df.index.drop(0)).reset_index(drop=True)
            df.columns.name = None
            # Writing the dataframe data to the csv file
            df.to_csv(self.file_name, index=False)

    def update_balance(self, balance):
        """Changes the value of the account balance stored in the file.

        Whenever a transaction is made, the resulting account balance in
        the file is changed to reflect the new balance.

        Parameters
        ----------
        balance : int
            The new account balance to be written to the file
        """
        self.update_file(balance, index=3)

    def edit_account_menu(self):
        """Displays a menu that allows registered users to change the
        stored details associated with their account."""

        def change_name():
            """Changes the account name stored in the file."""
            name = input("Enter new account name: ").lower()
            confirm_name = input(
                "Please enter new account name again: ").lower()
            while True:
                if name == confirm_name:
                    print("Account name successfully changed.")
                    self.update_file(name, index=0)
                    break
                else:
                    print("Account names don't match. Please try again.")
                    break

        def change_pin():
            """Changes the account PIN stored in the file."""
            pin = int(input("Enter new account PIN: "))
            confirm_pin = int(input("Please enter new account PIN again: "))
            while True:
                if pin == confirm_pin:
                    print("Account PIN successfully changed.")
                    self.update_file(pin, index=2)
                    break
                else:
                    print("Account PINs don't match. Please try again.")
                    break

        while True:
            print("\nPlease select an action "
                  "\n1---Change account name"
                  "\n2---Change account PIN")

            choices = {'1': change_name,
                       '2': change_pin}
            user_choice = choices.get(input())

            if user_choice is not None:
                user_choice()
                break
            else:
                print("Invalid choice. Please try again.")

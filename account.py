
class Account(object):
    """This class handles all the basic operations of a rudimentary bank account."""

    def __init__(self, account_name, account_id, account_balance,
                 deposit_amount, withdraw_amount, withdraw_limit, lower_limit=10000):
        self.account_name = account_name
        self.account_id = account_id
        self.account_balance = account_balance
        self.deposit_amount = deposit_amount
        self.withdraw_amount = withdraw_amount
        self.lower_limit = lower_limit
        self.withdraw_limit = withdraw_limit

    def display_balance(self):
        print(self.account_balance)

    def withdraw(self, withdraw_amount):
        self.account_balance -= withdraw_amount

    def deposit(self, deposit_amount):
        self.account_balance += deposit_amount

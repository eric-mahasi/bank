
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



    @property
    def account_name(self):
        return self.account_name

    @account_name.setter
    def account_name(self, account_name):
        self.account_name = account_name

    @property
    def account_id(self):
        return self.account_id

    @account_id.setter
    def account_id(self, account_ID):
        self.account_id = account_ID

    @property
    def account_balance(self):
        return self.account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        self.account_balance = account_balance

    @property
    def withdraw_limit(self):
        return self.withdraw_limit

    @withdraw_limit.setter
    def withdraw_limit(self, withdraw_limit):
        self.withdraw_limit = withdraw_limit

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        self.amount = amount

    def display_balance(self, account_balance):
        print(account_balance)

    def withdraw(self, withdraw_amount):
        self.account_balance -= self.withdraw_amount

    def deposit(self, deposit_amount):
        self.account_balance += self.deposit_amount

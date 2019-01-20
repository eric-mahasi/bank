class Account(object):
    """This class handles all the basic operations of a rudimentary bank account."""

    def __init__(self, account_name, account_id, deposit_amount, withdraw_amount, account_balance=1000):
        self.lower_limit = 1000
        self.account_name = account_name
        self.account_id = account_id
        self.account_balance = account_balance
        self.deposit_amount = deposit_amount
        self.withdraw_amount = withdraw_amount

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

    # FIXME account balance takes the value of 0

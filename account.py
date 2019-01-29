class Account(object):
    """
    This class handles all the basic operations of a rudimentary bank
    account.
    """
    LOWER_LIMIT = 1000

    def __init__(self, account_name, account_id, account_balance=1000):
        self.account_name = account_name
        self.account_id = account_id
        self.account_balance = account_balance

    # Suggestion: Instead of having this function carry out the logic of
    # getting user input, why not have this functionality in the bank Class
    # then pass the value to this function and process the value from there.

    # This function could throw an excepion if the withdraw_amount is greater
    # than the account_balance.
    def withdraw(self):
        prompt = "Please enter the amount you wish to withdraw: "
        withdraw_amount = int(input(prompt))
        if withdraw_amount >= self.account_balance:
            print(
                "Prohibited transaction. Account balances lower than "
                f"{self.LOWER_LIMIT} are not allowed. Please try again.")
        else:
            # TODO prevent account balances lower than lower limit
            self.account_balance -= withdraw_amount
            print(
                "Transaction successful. Your new account balance is "
                f"{self.account_balance}")

    # Suggestion: Instead of having this function carry out the logic of
    # getting user input, why not have this functionality in the bank Class
    # then pass the value to this function and process the value from there.
    def deposit(self):
        prompt = "Please enter the amount you wish to deposit: "
        deposit_amount = int(input(prompt))

        self.account_balance += deposit_amount
        print("Transaction successful. Your new account balance is",
              self.account_balance)

    # FIXME account balance takes the value of 0

    def print_account_balance(self):
        print(f"Your current account balance is: {self.account_balance}")

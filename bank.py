import account
import sys
b = account.Account("eric", 234, 10000, 54, 256, 50)


class Bank(object):
    """Driver class that runs the entire program."""

    def __init__(self, msg, user_choice):
        self.msg = 'Welcome user!\n' + '\nPlease select an action ' + \
            '\n1---Withdraw' + '\n2---Deposit' + '\n3---Check balance' + \
            '\n4---Exit'
        self.user_choice = user_choice

    def welcome_msg(self):
        print(self.msg)

    def evaluate_user_choice(self, user_choice):
        if self.user_choice == 1:
            # ask for amount use setter method use getter in next line
            b.amount = int(input("Please enter the amount you with to withdraw: "))
            b.withdraw(b.amount)
        elif self.user_choice == 2:
            # ask for amount use setter method use getter in next line
            b.amount = int(input("Please enter the amount you wish to deposit"))
            b.deposit(b.amount)
        elif self.user_choice == 3:
            # use getter method to display balance
            print("You current account balance is: ", b.account_balance)
        elif self.user_choice == 4:
            # quit the program
            sys.exit()
        else:
            # throw wrong input type error
            try:
                type(self.user_choice) != int
            except TypeError:
                print("Please make sure that you have typed a correct number")

        self.evaluate_user_choice(self.user_choice)


a = Bank(" ", 3)
a.welcome_msg()
a.evaluate_user_choice(4)

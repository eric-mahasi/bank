import account
import sys
# TODO create function to generate objects
# TODO choose proper names for objects and some variables
b = account.Account("eric", 234, 10000, 54, 256, 50)


class Bank(object):
    """Driver class that runs the entire program."""

# TODO figure out variables to be instantiated, if any necessary

    def display_welcome_msg(self):
        msg = 'Welcome user!\n' + '\nPlease select an action ' + \
              '\n1---Withdraw' + '\n2---Deposit' + '\n3---Check balance' + \
              '\n4---Exit'
        print(msg)

    def get_user_choice(self):
        self.user_choice = int(input())

    def evaluate_user_choice(self, user_choice):
        if user_choice == 1:
            b.withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
            b.withdraw(b.withdraw_amount)
        elif user_choice == 2:
            b.deposit_amount = int(input("Please enter the amount you wish to deposit: "))
            b.deposit(b.deposit_amount)
        elif user_choice == 3:
            print("You current account balance is: ", b.display_balance())
        elif user_choice == 4:
            print("Quitting... ")
            sys.exit()
        else:
            # TODO Handle errors for non-int inputs
            print("Invalid choice. Please try again: ")


a = Bank()
a.display_welcome_msg()
a.get_user_choice()
a.evaluate_user_choice(a.user_choice)

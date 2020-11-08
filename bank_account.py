# import random generator function
from random import randint

# create class that holds name address age
class AccountHolderDetails:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.age = int(input("Enter your age: "))

# create a class that represents a bank account with an account number and balance
class MyAccount(AccountHolderDetails):
    def __init__(self):
        super().__init__()
        self.account_number = 0
        self.balance = 0

    # Define a constructor method with account number and balance
    def constructor(self):
        # Generate a random 8 digit number for there account number
        self.account_number = int("".join([str(randint(0,9)) for x in range(8)]))
        print(f"Thanks for opening a new account!\nAccount number: {self.account_number}")
        # Try and ask how much the user wants to first deposit into the account
        try:
            self.balance = float(input("How much would you like to first deposit?\n=> £ "))
        except:
            print("Balance amount unrecognised. Account opened with £ 0.00.")
        finally:
            print("")

    # define a deposit method which manages deposit actions
    def deposit(self):
        #Changes self.balance to balance they have deposited
        try:
            self.balance += float(input("How much would you like to deposit?\n=> £ "))
        except:
            print("Amount not recognised.")
        finally:
            print(f"Your new balance is \n£ {self.balance}\n")

    # define a withdrawal method which manages withdrawal actions
    def withdrawal(self):
        # Display the amount the account holds
        print(f"Available balance: £ {self.balance}")
        # Changes self.balance depending on withdrawal amount and gives them the amount
        try:
            amount = float(input("How much would you like to withdraw?\n=> £ "))
            if amount > self.balance:
                print("I'm afraid you don't have the funds for that.")
            else:
                self.balance -= amount
                return amount
        except:
            print("Amount not recognised")
        finally:
            print(f"Your new balance is \n£ {self.balance}\n")

    # define a bank fees method that applies 5% off the balance
    def bank_fees(self):
        print("Bank fees of 5% are being applied to your balance")
        self.balance *= 0.95
        print(f"Your new balance is \n£ {self.balance}\n")

    # define display method to display account details
    def __str__(self):
        return f"""
Account Holder: {self.name}
Home Address:   {self.address}
Age:            {self.age}
Account number: {self.account_number}
Balance:        {self.balance}
        """

# define manage account class which is a child of my account class
class ManageAccount(MyAccount):
    def __init__(self):
        super().__init__()

    # Call all methods available
    def call_all_methods(self):
        self.constructor()
        self.deposit()
        cash = self.withdrawal()
        print(f"You have withdrawn \n£ {cash}\n")
        self.bank_fees()
        print(self)

if __name__ == "__main__":
    # Make an account object
    Account1 = ManageAccount()

    # Call all methods in account object
    Account1.call_all_methods()
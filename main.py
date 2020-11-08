# create class that holds name address age
class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    # create a print function for if you print the class object
    def __str__(self):
        print(f"Account Holder:{self.name}\nHome Address: {self.address}\nAge: {self.age}")

# create a class that represents a bank account with an account number and balance
class MyAccount(AccountHolderDetails):
    def __init__(self, account_number, balance):
        super().__init__()
        self.account_number = account_number
        self.balance = balance

    # define a constructor method with account number and balance
    def constructor(self):
        pass

    # define a deposit method which manages deposit actions
    def deposit(self):
        pass

    # define a withdrawal method which manages withdrawal actions
    def withdrawal(self):
        pass

    # define a bank fees method that applys 5% off the balance
    def bank_fees(self):
        pass

    # define display method to display account details
    def display(self):
        pass

# define manage account class which is a child of my account class
class ManageAccount(MyAccount):
    pass

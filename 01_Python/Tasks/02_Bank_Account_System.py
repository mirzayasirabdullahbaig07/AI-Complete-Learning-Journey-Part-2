# Define the Bank Account class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


# Creating a bank account
account1 = BankAccount("123456789")

# Testing the methods
account1.check_balance()     # Should print 0
account1.deposit(1000)       # Deposit 1000
account1.withdraw(300)       # Withdraw 300
account1.check_balance()     # Should print 700
account1.withdraw(800)       # Should show insufficient funds

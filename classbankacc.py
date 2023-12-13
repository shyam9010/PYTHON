class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")


# Example usage
account1 = BankAccount("John Doe", 1000)
account1.display_balance()

account1.deposit(500)
account1.withdraw(200)

account1.display_balance()

account1.withdraw(1500)  # This should display an error message about insufficient funds.

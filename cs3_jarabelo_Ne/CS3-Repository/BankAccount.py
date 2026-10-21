class BankAccount:
    def __init__(self,account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.__balance}"

account = BankAccount("Ana", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Current balance: {account.get_balance()}")
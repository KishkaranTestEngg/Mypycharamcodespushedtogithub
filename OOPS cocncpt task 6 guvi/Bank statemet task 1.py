class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   #  Encapsulation (private variable)

    #  method to access balance encapsulation (private variable)
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    # Protected method for subclasses
    def _update_balance(self, amount):
        self.__balance += amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    # Method to calculate and add interest
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self._update_balance(interest)
        print(f"Interest Added: {interest}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

 # Overriding withdraw method
    def withdraw(self, amount):
        if (self.get_balance() - amount) < self.minimum_balance:
            print("Cannot withdraw! Minimum balance requirement violated.")
        else:
            self._update_balance(-amount)
            print(f"Withdrawn: {amount}")

# Savings Account Test
print("=== Savings Account ===")
sa = SavingsAccount("SA001", 1000, 5)
sa.deposit(2500)
sa.calculate_interest()
print("Balance:", sa.get_balance())

print("------")

# Current Account Test
print("=== Current Account ===")
ca = CurrentAccount("CA001", 2000, 500)
ca.deposit(3500)
ca.withdraw(1800)   # Allowed
ca.withdraw(500)    # Not allowed (violates minimum balance)
print("Balance:", ca.get_balance())



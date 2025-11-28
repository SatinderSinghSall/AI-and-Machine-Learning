# OOP in Python: Encapsulation

class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # Public
        self.__balance = balance  # Private (Double Underscore → TRUE Private)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Satinder Singh Sall", 50000)
acc2 = BankAccount("Soni Vaibhav Kumar", 60000)

print(acc1.name)                   # Allowed
print(acc1.get_balance())          # Allowed through method

# print(acc1.__balance)            # ❌ Not allowed (private)
# print(acc2.__balance)            # ❌ Not allowed (private)

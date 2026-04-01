# OOP in Python: Abstraction Python

from abc import ABC, abstractmethod

class Payment(ABC):                     # Abstract Class
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} through Google Pay.")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit/Credit Card.")


p1 = UPI()
p2 = Card()

p1.pay(250)
p2.pay(800)

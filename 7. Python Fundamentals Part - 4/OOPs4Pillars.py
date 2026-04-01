# ---------------------------------------------
#  OOP in Python - 4 Pillars in One Codebase
# ---------------------------------------------

# 1️⃣ ENCAPSULATION
# Hiding data & controlling access using private variables

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.__balance


# 2️⃣ INHERITANCE
# Child class inherits features from parent class

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):      # Dog inherits Animal
    def bark(self):
        print("Dog barks")

class Cat(Animal):      # Cat also inherits Animal
    def meow(self):
        print("Cat meows")


# 3️⃣ POLYMORPHISM
# Same method name → different behavior

class Bird:
    def sound(self):
        print("Bird chirps")

class Duck(Bird):
    def sound(self):
        print("Duck quacks")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow tweets")


# 4️⃣ ABSTRACTION
# Hiding complex implementation using abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started with key ignition")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started with self start button")


# -----------------------------------------------------------
# USING ALL 4 PILLARS
# -----------------------------------------------------------

print("\n=== Encapsulation Example ===")
acc = BankAccount("Satinder", 5000)
acc.deposit(1500)
acc.withdraw(1000)
print("Current Balance:", acc.get_balance())


print("\n=== Inheritance Example ===")
d = Dog()
d.speak()
d.bark()

c = Cat()
c.speak()
c.meow()


print("\n=== Polymorphism Example ===")
for bird in [Duck(), Sparrow(), Bird()]:
    bird.sound()


print("\n=== Abstraction Example ===")
v1 = Car()
v2 = Bike()

v1.start()
v2.start()

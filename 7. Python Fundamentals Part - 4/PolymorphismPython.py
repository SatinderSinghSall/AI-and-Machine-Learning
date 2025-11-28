# OOP in Python: Polymorphism Python

# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Duck Typing
class Laptop:
    def run(self):
        print("Laptop Running...")

class Mobile:
    def run(self):
        print("Mobile Running...")


# Operator Overloading
class Values:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num


# OUTPUT DEMO
print("\n=== Polymorphism by Overriding ===")
for animal in [Animal(), Dog(), Cat()]:
    animal.sound()

print("\n=== Polymorphism by Duck Typing ===")
for device in [Laptop(), Mobile()]:
    device.run()

print("\n=== Operator Overloading ===")
v1 = Values(10)
v2 = Values(30)
print("Result (v1 + v2):", v1 + v2)

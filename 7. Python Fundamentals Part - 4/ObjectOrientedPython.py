# Object-Oriented Programming (OOP) in Python - Complete Tutorial (Basics to Advanced)

# 1. Creating a Class & Object
class Student:
    name = "Satinder"

s1 = Student()
print("Student Name:", s1.name)

# 2. __init__ Constructor
class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s2 = Student2("Satinder", 21)
print(s2.name, s2.age)

# 3. Instance & Class Variables
class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

c1 = Car("BMW")
c2 = Car("Audi")
print(c1.brand, c2.brand)
print(c1.wheels, c2.wheels)

# 4. Instance, Class, and Static Methods
class Student3:
    college = "KIIT"

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

    @classmethod
    def college_name(cls):
        print("College:", cls.college)

    @staticmethod
    def info():
        print("This is a Student class")

Student3.info()
Student3.college_name()
s3 = Student3("Satinder")
s3.show()

# 5. Encapsulation
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show(self):
        print("Balance:", self.__balance)

acc = Bank()
acc.deposit(500)
acc.show()

# 6. Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# 7. Polymorphism - Function Overriding
class Animal2:
    def sound(self):
        print("General sound")

class Cat(Animal2):
    def sound(self):
        print("Meow")

Cat().sound()

# 8. Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

c = Circle(5)
print("Area:", c.area())

# 9. Magic Methods
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book with {self.pages} pages"

    def __len__(self):
        return self.pages

b = Book(120)
print(b)
print(len(b))

# 10. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 1)
p3 = p1 + p2
print(p3.x, p3.y)

# 11. Access Modifiers
class Test:
    a = 1      # public
    _b = 2     # protected
    __c = 3    # private

# 12. Composition (has-a relationship)
class Engine:
    def start(self):
        print("Engine running")

class Car2:
    def __init__(self):
        self.engine = Engine()

    def run(self):
        self.engine.start()

car = Car2()
car.run()

# 13. Multiple Inheritance + MRO
class A:
    def show(self): print("A")

class B:
    def show(self): print("B")

class C(A, B):
    pass

obj = C()
obj.show()
print(C.mro())

# END OF OOP COMPLETE FILE

# -----------------------------------------------
# OOP IN PYTHON: TYPES OF INHERITANCE IN ONE FILE
# -----------------------------------------------

# 1️⃣ SINGLE INHERITANCE (One parent → one child)
class Vehicle:
    def show_vehicle(self):
        print("This is a vehicle")

class Car(Vehicle):  # Inherits Vehicle
    def show_car(self):
        print("This is a Car")


# 2️⃣ MULTILEVEL INHERITANCE (Grandparent → Parent → Child)
class LivingBeing:
    def breathe(self):
        print("Living beings breathe")

class Animal(LivingBeing):  # Inherits LivingBeing
    def eat(self):
        print("Animals eat food")

class Dog(Animal):  # Inherits Animal (multi-level chain)
    def bark(self):
        print("Dog barks")


# 3️⃣ MULTIPLE INHERITANCE (Child inherits from 2 parents)
class Father:
    def father_feature(self):
        print("Father: Hardworking")

class Mother:
    def mother_feature(self):
        print("Mother: Caring")

class Child(Father, Mother):   # Inherits from both Father + Mother
    def child_feature(self):
        print("Child: Gets both qualities")


# 4️⃣ HIERARCHICAL INHERITANCE (One parent → many children)
class Shape:
    def show_shape(self):
        print("This is a geometric shape")

class Circle(Shape):
    def draw_circle(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw_square(self):
        print("Drawing a Square")

class Triangle(Shape):
    def draw_triangle(self):
        print("Drawing a Triangle")


# 5️⃣ HYBRID INHERITANCE (Combination of inheritances)
#    Example: A Teacher is an Employee + also a LivingBeing

class Employee:
    def work(self):
        print("Employee works in an organization")

class Teacher(Employee, LivingBeing):    # Inherits multiple + part of hierarchy
    def teach(self):
        print("Teacher teaches students")


# ---------------------------------------------------------------
#               OBJECT CREATION & OUTPUT DEMONSTRATION
# ---------------------------------------------------------------

print("\n===== 1️⃣ Single Inheritance =====")
car = Car()
car.show_vehicle()
car.show_car()

print("\n===== 2️⃣ Multilevel Inheritance =====")
dog = Dog()
dog.breathe()
dog.eat()
dog.bark()

print("\n===== 3️⃣ Multiple Inheritance =====")
child = Child()
child.child_feature()
child.father_feature()
child.mother_feature()

print("\n===== 4️⃣ Hierarchical Inheritance =====")
c1 = Circle()
s1 = Square()
t1 = Triangle()

c1.show_shape(); c1.draw_circle()
s1.show_shape(); s1.draw_square()
t1.show_shape(); t1.draw_triangle()

print("\n===== 5️⃣ Hybrid Inheritance =====")
teacher = Teacher()
teacher.breathe()
teacher.work()
teacher.teach()

# Methods in Python - Instance, Class and Static in OOP

class Student:

    college = "KIIT"     # class variable

    def __init__(self, name, course):
        self.name = name         # instance variable
        self.course = course

    # Instance Method
    def show(self):
        print(f"Name: {self.name}, Course: {self.course}")

    # Class Method
    @classmethod
    def changeCollege(cls, newCollege):
        cls.college = newCollege
        print("College updated to:", cls.college)

    # Static Method
    @staticmethod
    def info():
        print("This is the Student class.")


# Creating object
s1 = Student("Satinder", "MCA")

# Calling methods
s1.show()                 # instance method
Student.changeCollege("BPUT")  # class method
Student.info()            # static method

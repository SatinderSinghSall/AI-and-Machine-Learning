# Attributes - class & Instance: OOP Python

class Student:
    collageName = "KiiT University"
    
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Satinder", 9)
stu2 = Student("Vaibhav", 8)

print(stu1.name, stu1.cgpa)
print(stu1.name, stu2.cgpa)

# Object Oriented Programming: Constructor - init() Method

# Class
class student:
    # Only use single constructor in a class
    def __init__(self, name, year, course, roll_no, cgpa):
        print("A Constructor was called!")
        self.name = name
        self.year = year
        self.course = course
        self.roll_no = roll_no
        self.cgpa = cgpa
        
    def getCGPA(self):
        return self.cgpa

# Object
stu1 = student("Satinder Singh Sall", 1, "MCA", 180, 8.5)
stu2 = student("Soni Vaibhav Kumar", 1, "MCA", 207, 9.9)

print(stu1.name, stu1.year, stu1.course, stu1.roll_no)
print(stu2.name, stu2.year, stu2.course, stu2.roll_no)

print(f"CGPA of {stu1.name} is {stu1.getCGPA()}")
print(f"CGPA of {stu2.name} is {stu2.getCGPA()}")

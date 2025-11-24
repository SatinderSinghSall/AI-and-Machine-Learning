# Object Oriented Programming: Constructor - init() Method

# Class
class student:
    def __init__(self, name, year, course, roll_no):
        print("A Constructor was called!")
        self.name = name
        self.year = year
        self.course = course
        self.roll_no = roll_no

# Object
stu1 = student("Satinder Singh Sall", 1, "MCA", 180)
stu2 = student("Soni Vaibhav Kumar", 1, "MCA", 207)

print(stu1.name, stu1.year, stu1.course, stu1.roll_no)
print(stu2.name, stu2.year, stu2.course, stu2.roll_no)

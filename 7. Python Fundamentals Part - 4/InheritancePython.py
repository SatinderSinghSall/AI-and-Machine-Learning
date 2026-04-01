# OOP in Python: Inheritance

class Employee:
    startTime = "10:00 AM"
    endTime   = "06:00 PM"
    company   = "TechVerse Pvt. Ltd."

    def changeTime(self, new_end_time):
        Employee.endTime = new_end_time   # Applies to all Employees

    def get_employee_details(self):
        print("\n────────── Employee Details ──────────")
        print(f"Company       : {self.company}")
        print(f"Work Time     : {self.startTime} → {self.endTime}")


class Teachers(Employee):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def info(self):
        self.get_employee_details()
        print(f"Role          : Teacher")
        print(f"Teaches       : {self.subject}")
        print("─────────────────────────────────────")


class AdminStaff(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        self.get_employee_details()
        print(f"Role          : Admin Staff")
        print(f"Department    : {self.role}")
        print("─────────────────────────────────────")


# ───────────────────────────────#
# Creating Employee Objects
# ───────────────────────────────#
t1 = Teachers("Satinder Singh Sall", "Data Structures & Algorithms")
a1 = AdminStaff("Soni Vaibhav Kumar", "Operations Manager")

# Changing work time for entire organization
t1.changeTime("06:30 PM")

# Displaying Information
t1.info()
a1.info()

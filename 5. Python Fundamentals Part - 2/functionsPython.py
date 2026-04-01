# -----------------------------------------
# 1. Basic Function
# -----------------------------------------
def greeting():
    print("Hello, World!")

greeting()


# -----------------------------------------
# 2. Function with Parameters & Return
# -----------------------------------------
def sumNums(num1, num2):
    sum_val = num1 + num2
    return sum_val

print(sumNums(1, 1))


# -----------------------------------------
# 3. Function to find Average
# -----------------------------------------
def avgNums(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg

print(avgNums(1, 1, 1))


# -----------------------------------------
# 4. Default Arguments
# -----------------------------------------
def greetUser(name="User"):
    print("Hello,", name)

greetUser()
greetUser("Satinder")


# -----------------------------------------
# 5. Keyword Arguments
# -----------------------------------------
def student(name, age):
    print("Name:", name, " Age:", age)

student(age=21, name="Rahul")


# -----------------------------------------
# 6. *args (Unlimited Positional Arguments)
# -----------------------------------------
def total(*numbers):
    print("Sum:", sum(numbers))

total(1, 2, 3, 4, 5)


# -----------------------------------------
# 7. **kwargs (Unlimited Keyword Arguments)
# -----------------------------------------
def showInfo(**info):
    print(info)

showInfo(name="Ravi", age=22, city="Delhi")


# -----------------------------------------
# 8. Lambda (Anonymous Functions)
# -----------------------------------------
square = lambda x: x * x
print("Square:", square(5))

add = lambda a, b: a + b
print("Add:", add(3, 4))


# -----------------------------------------
# 9. Higher Order Functions
# -----------------------------------------
def applyFunction(func, value):
    return func(value)

print(applyFunction(lambda n: n * n, 6))


# -----------------------------------------
# 10. Built-in map(), filter(), reduce()
# -----------------------------------------
nums = [1, 2, 3, 4, 5]

# map
square_list = list(map(lambda x: x * x, nums))
print("Map:", square_list)

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Filter:", evens)

# reduce
from functools import reduce
total_sum = reduce(lambda a, b: a + b, nums)
print("Reduce:", total_sum)


# -----------------------------------------
# 11. Recursion
# -----------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# -----------------------------------------
# 12. Docstring (Documentation)
# -----------------------------------------
def addNums(a, b):
    """This function returns the sum of two numbers."""
    return a + b

print(addNums.__doc__)


# -----------------------------------------
# 13. Closures (Function inside a Function)
# -----------------------------------------
def outer(message):
    def inner():
        print("Inner says:", message)
    return inner

msg = outer("Hello from Closure!")
msg()


# -----------------------------------------
# 14. Decorators
# -----------------------------------------
def myDecorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@myDecorator
def sayHello():
    print("Hello from inside the function!")

sayHello()

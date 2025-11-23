'''
    Take two numbers as input from the user and print their:
    sum, difference, product, and quotient
'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print(num1, "+", num2, "=", sum)
print(num1, "-", num2, "=", difference)
print(num1, "*", num2, "=", product)
print(num1, "/", num2, "=", quotient)

# Odd or Even Number Program

num = int(input("Enter a number: "))

odd = num % 2 != 0

if odd:
    print(f"The number {num} is an ODD number.")
else:
    print(f"The number {num} is an EVEN number.")

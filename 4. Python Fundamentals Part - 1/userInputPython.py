# ================================================
#         USER INPUT IN PYTHON - FULL DEMO
# ================================================

print("\n===== 1. BASIC INPUT =====")
name = input("Enter your name: ")
print("Hello,", name)


print("\n===== 2. INTEGER INPUT =====")
age = int(input("Enter your age: "))
print("Your age is:", age)


print("\n===== 3. FLOAT INPUT =====")
price = float(input("Enter price: "))
print("Price entered:", price)


print("\n===== 4. MULTIPLE INPUTS =====")
a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)


print("\n===== 5. LIST INPUT =====")
numbers = list(map(int, input("Enter numbers: ").split()))
print("List =", numbers)


print("\n===== 6. CHARACTER INPUT =====")
ch = input("Enter a character: ")[0]
print("Character:", ch)


print("\n===== 7. BOOLEAN INPUT =====")
flag = input("Enter True/False: ").strip().lower() == "true"
print("Boolean:", flag)


print("\n===== 8. DEFAULT VALUE TRICK =====")
value = input("Enter value (default = 100): ") or "100"
print("Value =", value)

# ================================================
print("\n===== END OF INPUT DEMO =====")

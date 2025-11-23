# ========================================================
#          ALL PYTHON TYPE CONVERSIONS IN ONE CODEBASE
# ========================================================

print("\n===== 1. IMPLICIT TYPE CONVERSION =====")
a = 5       # int
b = 2.5     # float
c = a + b
print("a + b =", c, "| type:", type(c))

x = True
y = 10
print("True + 10 =", x + y, "| type:", type(x + y))


# --------------------------------------------------------

print("\n===== 2. EXPLICIT TYPE CONVERSION =====")

print("\n--- int() examples ---")
print(int(5.99))         # float → int
print(int("20"))         # str → int

# invalid: int("10.5")  # would cause error

print("\n--- float() examples ---")
print(float(5))          # int → float
print(float("3.14"))     # str → float

print("\n--- str() examples ---")
print(str(123))          # int → str
print(str(3.14))         # float → str

print("\n--- bool() examples ---")
print(bool(0))           # False
print(bool(1))           # True
print(bool(""))          # False
print(bool("Python"))    # True

print("\n--- list(), tuple(), set() examples ---")
print(list("abc"))           # str → list
print(tuple([1, 2, 3]))       # list → tuple
print(set([1, 2, 2, 3]))      # list → set (removes duplicates)

print("\n--- complex() examples ---")
print(complex(5))        # 5 + 0j
print(complex(3, 4))     # 3 + 4j


# --------------------------------------------------------

print("\n===== 3. TYPE CONVERSION WITH input() =====")
# NOTE: input() always returns string.
# Uncomment to test interactively.

# age = int(input("Enter age: "))
# height = float(input("Enter height: "))
# print("Age:", age, "| type:", type(age))
# print("Height:", height, "| type:", type(height))


# --------------------------------------------------------

print("\n===== 4. DANGEROUS / TRICKY CONVERSIONS =====")
print("int(9.99) =", int(9.99))     # truncates
# print(int("5a"))  # ERROR
print("bool([]) =", bool([]))       # empty = False
print("bool([1]) =", bool([1]))     # non-empty = True


# --------------------------------------------------------

print("\n===== 5. CHECKING TYPES BEFORE CONVERSION =====")
value = "123"
if value.isdigit():
    print("Safe to convert:", int(value))
else:
    print("Not safe to convert!")


# ========================================================
print("\n===== END OF TYPE CONVERSION DEMO =====")

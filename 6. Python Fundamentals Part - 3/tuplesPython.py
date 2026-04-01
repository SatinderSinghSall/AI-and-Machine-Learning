# Python Tuples - Complete Tutorial (Basics to Advanced)

# 1. Basic Tuple Declaration
tuple1 = (10, 20, 30, 40)
print("Tuple:", tuple1)
print("Type:", type(tuple1))
print("Length:", len(tuple1))

# 2. Tuple with Multiple Data Types
tuple2 = ("Satinder", 180, 5.8, True)
print("\nMixed Tuple:", tuple2)

# 3. Accessing Tuple Elements
print("\nAccessing Elements:")
print(tuple1[0])
print(tuple1[-1])
print(tuple1[1:3])

# 4. Tuples are Immutable
# tuple1[0] = 99  # This will cause an error

# 5. Creating a Tuple Without Parentheses
tuple3 = 1, 2, 3
print("\nTuple without parentheses:", tuple3)

# Special Case: Single Element Tuple
single = (10,)
print("Single element tuple:", single)

# 6. Looping Through Tuples
print("\nLooping:")
for item in tuple1:
    print(item, end=" ")
print()

# 7. Tuple Functions
print("\nFunctions:")
print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))

# 8. Tuple Packing and Unpacking
tuple4 = (100, 200, 300)
a, b, c = tuple4
print("\nUnpacked Values:", a, b, c)

# 9. Nested Tuples
nested = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple:", nested[1][1])

# 10. Tuple Methods
print("\nTuple Methods:")
tuple5 = (10, 20, 30, 20, 20, 40)
print(tuple5.count(20))
print(tuple5.index(30))

# 11. Using Tuples in Real-World Scenario
# Returning multiple values from a function
def student_details():
    name = "Satinder"
    age = 23
    course = "MCA"
    return name, age, course

info = student_details()
print("\nStudent Details Tuple:", info)

# 12. Tuple vs List Comparison
print("\nTuple vs List:")
tup = (1, 2, 3)
lst = [1, 2, 3]
print("Tuple is immutable, List is mutable")
print("Tuple:", tup)
print("List before update:", lst)
lst[0] = 99
print("List after update:", lst)

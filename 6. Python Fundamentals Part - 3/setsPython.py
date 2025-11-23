# Python Sets - Complete Tutorial (Basics to Advanced)

# 1. Basic Set Declaration
set1 = {10, 20, 30, 40}
print("Set:", set1)
print("Type:", type(set1))
print("Length:", len(set1))

# Sets automatically remove duplicates
set2 = {10, 20, 20, 30, 30}
print("\nDuplicate Removal:", set2)

# 2. Creating a Set Using set()
set3 = set([1, 2, 3, 4])
print("\nSet using set():", set3)

# 3. Adding Elements
numbers = {1, 2, 3}
numbers.add(4)
numbers.update([5, 6, 7])
print("\nAfter Adding Elements:", numbers)

# 4. Removing Elements
numbers.discard(7)         # Won't give error if element missing
numbers.remove(6)          # Will give error if element missing
removed = numbers.pop()    # Removes random element
print("\nAfter Removing:", numbers)
print("Removed Random Element:", removed)

# 5. Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nSet Operations:")
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric Difference:", A ^ B)

# 6. Looping Through Sets
print("\nLooping:")
for x in set1:
    print(x, end=" ")
print()

# 7. Checking Membership
print("\nMembership:")
print(10 in set1)
print(50 in set1)

# 8. Frozenset (Immutable Set)
frozen = frozenset([10, 20, 30])
print("\nFrozenset:", frozen)

# 9. Set Comprehension
squares = {x*x for x in range(1, 6)}
print("\nSet Comprehension:", squares)

# 10. Removing Duplicates from a List Using Set
nums = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(nums)
print("\nUnique Elements:", unique_set)

# Convert back to list
unique_list = list(unique_set)
print("List from Set:", unique_list)

# 11. Real-World Example: Find Common Students
classA = {"Aman", "Riya", "Karan", "John"}
classB = {"Riya", "Simran", "John", "Ankit"}

print("\nCommon Students:", classA & classB)
print("Students Only in Class A:", classA - classB)
print("All Students:", classA | classB)

# Python Lists - Complete Tutorial (Basics to Advanced)

# 1. Basic List Declaration
marks = [99, 12, 44, 32, 42, 24]

print("Length of marks list:", len(marks))
print("Marks:", marks)
print("First element:", marks[0])

# Updating a list value
marks[2] = 100
print("Updated marks:", marks)

# Multiple Data Types in a List
student = ["Satinder Singh Sall", 'C', 180, "MCA"]
print("Student list:", student)
print("Student name:", student[0])
print("Type of student:", type(student))


# 2. List Indexing & Slicing
nums = [10, 20, 30, 40, 50, 60]
print("\nIndexing & Slicing Examples:")
print(nums[1])          # Positive indexing
print(nums[-1])         # Negative indexing
print(nums[1:4])        # Slicing
print(nums[:3])         # Start to index 3
print(nums[3:])         # Index 3 to end
print(nums[::2])        # Step slicing


# 3. Adding Elements
fruits = ["Apple", "Banana"]
print("\nBefore adding elements:", fruits)
fruits.append("Mango")
fruits.insert(1, "Orange")
fruits.extend(["Grapes", "Pineapple"])
print("After adding elements:", fruits)


# 4. Removing Elements
fruits.remove("Orange")            # Remove by value
fruits.pop(2)                       # Remove at index
removed_item = fruits.pop()        # Remove last element
print("After removing elements:", fruits)
print("Removed item:", removed_item)

del fruits[0]                       # Delete using del
print("After del operation:", fruits)

fruits.clear()                      # Clear list
print("After clear():", fruits)


# 5. Looping Through List
numbers = [1, 2, 3, 4, 5]
print("\nLooping through list:")

for num in numbers:
    print(num, end=" ")
print()

for i in range(len(numbers)):
    print(numbers[i], end=" ")
print()


# 6. Searching in List
search_list = [10, 20, 30, 40, 50, 30]
print("\nSearching:")
print(30 in search_list)           # Using 'in'
print(search_list.count(30))       # Count occurrences
print(search_list.index(40))       # Get index


# 7. Sorting & Reversing
values = [5, 1, 4, 3, 2]
values.sort()                      # Ascending
print("\nSorted list:", values)
values.sort(reverse=True)          # Descending
print("Descending order:", values)

values.reverse()                   # Reverse list
print("Reversed:", values)


# 8. List Comprehension
squares = [x*x for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
print("\nList Comprehensions:")
print("Squares:", squares)
print("Even numbers:", evens)


# 9. Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nNested list element:", matrix[1][2])


# 10. Copying Lists
original = [10, 20, 30]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]
print("\nCopied Lists:")
print(copy1, copy2, copy3)


# 11. Unpacking Lists
a, b, c = [10, 20, 30]
print("\nUnpacked values:", a, b, c)


# 12. Using * Operator
nums_multiplied = [1, 2, 3] * 3
print("\nList multiplied:", nums_multiplied)


# 13. Using zip() with Lists
names = ["A", "B", "C"]
ages = [21, 22, 23]
print("\nUsing zip():")
for name, age in zip(names, ages):
    print(name, age)


# 14. Real-World Program: Remove Duplicates
nums_dup = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in nums_dup:
    if n not in unique:
        unique.append(n)

print("\nList without duplicates:", unique)

# 15. Find an element in a list:
numsList = [12, 23, 32, 180, 207]
ele = 180
idx = 0
for val in numsList:
    if val == ele:
        print(f"Found the element {ele} at index {idx}")
        break
    idx = idx + 1

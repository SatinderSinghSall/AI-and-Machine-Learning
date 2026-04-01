# Python Dictionaries - Complete Tutorial (Basics to Advanced)

# 1. Basic Dictionary Declaration
student = {
    "name": "Satinder",
    "age": 23,
    "course": "MCA"
}
print("Dictionary:", student)
print("Type:", type(student))
print("Length:", len(student))

# 2. Accessing Dictionary Values
print("\nAccessing Values:")
print(student["name"])           # Using key
print(student.get("age"))         # Using get()

# 3. Adding & Updating Values
student["age"] = 24
student["city"] = "Bhubaneswar"
print("\nAfter Update:", student)

# 4. Removing Items
student.pop("city")               # Remove key-value
removed = student.popitem()       # Removes last inserted
print("\nAfter Removal:", student)
print("Removed Item:", removed)

# 5. Looping Through Dictionary
print("\nLooping:")
for key in student:
    print(key, "=", student[key])

print("\nLooping keys():")
for k in student.keys():
    print(k)

print("\nLooping values():")
for v in student.values():
    print(v)

print("\nLooping items():")
for k, v in student.items():
    print(k, "=", v)

# 6. Checking Existence
print("\nChecking Keys:")
print("name" in student)
print("city" in student)

# 7. Dictionary Methods
print("\nDictionary Methods:")
print(student.keys())
print(student.values())
print(student.items())

# 8. Nested Dictionaries
students = {
    "student1": {"name": "Satinder", "age": 23},
    "student2": {"name": "Aman", "age": 24}
}
print("\nNested Dictionary:", students["student2"]["age"])

# 9. Copying Dictionaries
copy1 = student.copy()
copy2 = dict(student)
print("\nCopied Dictionaries:")
print(copy1)
print(copy2)

# 10. Using update() Method
student.update({"roll": 180})
print("\nAfter update():", student)

# 11. Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary Comprehension:", squares)

# 12. Real-World Use Case
products = [
    {"id": 1, "name": "Laptop", "price": 60000},
    {"id": 2, "name": "Keyboard", "price": 1200},
    {"id": 3, "name": "Mouse", "price": 600}
]

print("\nProduct Details:")
for p in products:
    print(p["name"], "- Rs", p["price"])

# 13. Converting Two Lists into a Dictionary
keys = ["name", "age", "course"]
values = ["Satinder", 23, "MCA"]

combined = dict(zip(keys, values))
print("\nDictionary from two lists:", combined)

# 14. Clear Dictionary
new_dict = {"a": 1, "b": 2}
new_dict.clear()
print("\nAfter clear():", new_dict)

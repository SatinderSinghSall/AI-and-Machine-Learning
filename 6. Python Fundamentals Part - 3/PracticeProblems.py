# Practice Problems:

info = [
    ("Satinder", "MAth"),
    ("Vaibhav", "Science"),
    ("Swayam", "Science"),
    ("Harsha HM", "Math"),
    ("Santosh", "MAth"),
    ("Yati", "English"),
    ("Nick", "English"),
]

unique_courses = set()

for name, course in info:
    print(name, course)
    if course == 'English':
        print(course)

print("\n")

dict = {}
for name, course in info:
    if dict.get(name == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)

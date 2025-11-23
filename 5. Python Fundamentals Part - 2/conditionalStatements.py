# Voting Eligibility System:

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print()

if age < 0:
    print("Invalid age.")
elif age < 13:
    print(f"Dear {name}, you are a child.")
elif age < 18:
    print(f"Dear {name}, you are a teenager. You cannot vote yet.")
elif age <= 60:
    print(f"Dear {name}, you are an adult. You can vote.")
else:
    print(f"Dear {name}, you are a senior citizen and can vote.")

print("Welcome to the Eligibility Checker")

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

if age >= 18:                # Outer condition
    if has_id == "yes":      # Inner condition
        print("You are allowed to enter.")
    else:
        print("You must bring a valid ID.")
else:
    print("You are underage.")

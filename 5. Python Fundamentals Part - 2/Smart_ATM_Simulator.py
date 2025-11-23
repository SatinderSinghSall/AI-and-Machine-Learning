# Mini Project: Smart ATM Simulator (Beginner–Friendly, Uses Conditions Only)

print("🏧 Welcome to Python Bank ATM")

# Step 1: Hardcoded PIN and balance
PIN = 1234
balance = 5000

# Step 2: User enters PIN
entered_pin = int(input("Enter your ATM PIN: "))

if entered_pin == PIN:
    print("Login successful!\n")
    
    # Step 3: ATM Menu
    print("Select an option:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Step 4: Conditions for Menu
    if choice == 1:
        print(f"Your balance is ₹{balance}")

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! New balance: ₹{balance}")
        else:
            print("❌ Insufficient balance!")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposit successful! New balance: ₹{balance}")
        else:
            print("❌ Invalid amount!")

    elif choice == 4:
        print("Thank you for using Python Bank ATM 😊")

    else:
        print("❌ Invalid option! Please select between 1-4.")

else:
    print("❌ Incorrect PIN! Access denied.")


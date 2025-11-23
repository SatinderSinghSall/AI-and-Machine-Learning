username = input("Enter username: ")
password = input("Enter password: ")

# Hardcoded credentials
admin_user = "admin"
admin_pass = "admin123"

normal_user = "user"
normal_pass = "user123"

if username == admin_user and password == admin_pass:
    print("Login successful! Welcome Admin 👑")
elif username == normal_user and password == normal_pass:
    print("Login successful! Welcome User 😊")
else:
    print("Invalid credentials ❌")

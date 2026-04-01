# Q4: User enters a string containing a number. 
# Convert it to int, float, and string again.

userPrompt = input("Enter a number: ")

# converting types
userPrompt_int = int(userPrompt)
userPrompt_float = float(userPrompt)
userPrompt_string = str(userPrompt)

# printing values and their types
print("\nConverted Values:")
print("Integer: ", userPrompt_int, "| Type:", type(userPrompt_int))
print("Float:   ", userPrompt_float, "| Type:", type(userPrompt_float))
print("String:  ", userPrompt_string, "| Type:", type(userPrompt_string))

principalAmount = float(input("Enter the principal amount: "))
rateOfInterest = float(input("Enter the rate of interest (%): "))
timeYears = float(input("Enter the time in years: "))

simpleInterest = (principalAmount * rateOfInterest * timeYears) / 100

print("\n--- Simple Interest Calculation ---")
print("Principal Amount:", principalAmount)
print("Rate of Interest:", rateOfInterest)
print("Time (Years):", timeYears)
print("Simple Interest =", simpleInterest)

color = input("Enter a traffic light color (Red / Yellow / Green) : ").lower()

if color == "red":
    print("🛑 STOP")
elif color == "yellow":
    print("⚠️  SLOW DOWN")
elif color == "green":
    print("🟢 GO")
else:
    print("❌ Invalid color! Please enter Red, Yellow, or Green.")

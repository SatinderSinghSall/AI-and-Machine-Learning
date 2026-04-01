# break & continue in Python:

i = 1
while i <= 10:
    if i == 5:
        break
    print(f"Number: {i}")
    i = i + 1
print("LOOP EXITED")

j = 1
while j <= 10:
    if j == 5:
        j = j + 1
        continue
    print(f"Number: {j}")
    j = j + 1
print("LOOP EXITED")

# Even Numbers from 1 to 10:
num = 1
while(num <= 10):
    if(num % 2 == 0):
        print(num)
    num = num + 1

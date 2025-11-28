# File Handling/Operations in Python:

# f = open(r"E:\Apna Collage - Prime AI - ML\8. Python Fundamentals Part - 5\Test Files\sample.txt", "r")

# # read() – Read full content
# data = f.read()
# print(data)

# # readLine() – Read one line at a time
# data = f.readline()
# print(data)

# write() - To write in a file (Change/Update mode to write w & it clears the old data and add the new ones)
# f = open(r"E:\Apna Collage - Prime AI - ML\8. Python Fundamentals Part - 5\Test Files\sample.txt", "w")
# f.write("Currently I am pursuing\nMy MCA degree from\nKiiT University, Bhubaneswar, Odisha, India.")

# append() - To add the data from the end (it does not clear the old data, it adds them from the end)
f = open(r"E:\Apna Collage - Prime AI - ML\8. Python Fundamentals Part - 5\Test Files\sample.txt", "a")
f.write("\n\nMy skills:\n1. Full-Stack Development.\n2. Mobile App Development (Android / iOS)\n3. DevOps / Cloud Engg")

f.close()

# Strings in Python - Complete Tutorial (Basics to Advanced)

# 1. String Declaration
s1 = "Hello"
s2 = 'World'
s3 = """This is a multiline string"""
print(s1, s2, s3)

# 2. Indexing
s = "Python"
print(s[0])
print(s[-1])

# 3. Slicing
print(s[0:3])
print(s[2:])
print(s[::-1])  # reverse

# 4. Length
print(len(s))

# 5. Immutability
s = "Hello"
s = "M" + s[1:]
print(s)

# 6. Looping
for ch in "ABC":
    print(ch)

# 7. String Methods
text = "hello world"
print(text.upper())
print(text.title())
print(text.find("world"))
print(text.replace("world", "Python"))
print(text.count("l"))
print(text.startswith("hello"))

# 8. Split and Join
line = "apple,banana,grapes"
fruits = line.split(",")
print(fruits)
print(" - ".join(fruits))

# 9. Strip
msg = "   hi there   "
print(msg.strip())

# 10. Formatting
name = "Satinder"
age = 22
print(f"My name is {name} and I am {age} years old.")

# 11. Escape Characters
print("Hello\nWorld")
print("He said \"Python!\"")

# 12. Raw Strings
path = r"C:\\Users\\Desktop"
print(path)

# 13. Check String Types
x = "123abc"
print(x.isdigit())
print(x.isalnum())

# 14. Comparison
print("apple" < "banana")

# 15. Interning
A = "hello"
B = "hello"
print(A is B)

# 16. Encoding & Decoding
encoded = "Hello".encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))

# 17. Regex
import re
text = "My phone number is 98765-43210"
match = re.search(r"\\d{5}-\\d{5}", text)
if match:
    print("Found:", match.group())

# 18. String Concatenation & Repetition
print("Hello" + " " + "World")
print("ha" * 3)

# 19. Character Encoding
print(ord('A'))
print(chr(65))

# 20. Case-Insensitive Comparison
print("Python".lower() == "PYTHON".lower())

# 21. String Justification
print("hi".ljust(10, '-'))
print("hi".rjust(10, '-'))
print("42".zfill(5))

# 22. String Translation
trans = str.maketrans({'a': '@', 'e': '3'})
print("apple".translate(trans))

# 23. Checking Prefixes & Suffixes
print("document.pdf".endswith((".pdf", ".txt")))

# 24. Unicode Normalization
import unicodedata
s_uni = "café"
s_norm = unicodedata.normalize('NFC', s_uni)
print(s_norm)

# 25. Advanced f-string Expressions
value = 5
print(f"Value squared = {value**2}")

# 26. String Comparison Using locale
import locale
locale.setlocale(locale.LC_ALL, "C")
print(locale.strcoll("apple", "banana"))

# 27. Remove Punctuation
import string
text = "Hello!!! How are you???"
clean = text.translate(str.maketrans('', '', string.punctuation))
print(clean)

# 28. Extract Numbers
nums = re.findall(r"\\d+", "My id is 123 and age is 22")
print(nums)

# 29. Find All Capital Words
words = re.findall(r"[A-Z][a-z]*", "Satinder lives in India and studies Computer Science")
print(words)

# 30. Reverse Words in a Sentence
sentence = "Python is amazing"
print(" ".join(sentence.split()[::-1]))

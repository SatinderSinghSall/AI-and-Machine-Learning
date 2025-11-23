# ========================================================
#          ALL PYTHON OPERATORS IN ONE CODEBASE
# ========================================================

print("\n===== 1. ARITHMETIC OPERATORS =====")
a, b = 10, 3
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)

# --------------------------------------------------------

print("\n===== 2. ASSIGNMENT OPERATORS =====")
x = 5
print("x =", x)
x += 2
print("x += 2 →", x)
x -= 1
print("x -= 1 →", x)
x *= 3
print("x *= 3 →", x)
x /= 2
print("x /= 2 →", x)
x //= 2
print("x //=2 →", x)
x %= 3
print("x %= 3 →", x)
x **= 2
print("x **=2 →", x)

# --------------------------------------------------------

print("\n===== 3. COMPARISON OPERATORS =====")
p, q = 7, 10
print("p == q →", p == q)
print("p != q →", p != q)
print("p > q  →", p > q)
print("p < q  →", p < q)
print("p >= q →", p >= q)
print("p <= q →", p <= q)

# --------------------------------------------------------

print("\n===== 4. LOGICAL OPERATORS =====")
a, b = True, False
print("a and b →", a and b)
print("a or b  →", a or b)
print("not a   →", not a)

# --------------------------------------------------------

print("\n===== 5. MEMBERSHIP OPERATORS =====")
text = "Satinder"
print("'a' in text →", 'a' in text)
print("'z' not in text →", 'z' not in text)

# --------------------------------------------------------

print("\n===== 6. IDENTITY OPERATORS =====")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 →", list1 is list2)   # Same memory
print("list1 is list3 →", list1 is list3)   # Different memory
print("list1 == list3 →", list1 == list3)   # Same value

# --------------------------------------------------------

print("\n===== 7. BITWISE OPERATORS =====")
a, b = 10, 4   # 10 = 1010, 4 = 0100
print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

# --------------------------------------------------------

print("\n===== 8. TERNARY OPERATOR =====")
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print("7 is", result)

# --------------------------------------------------------

print("\n===== 9. OPERATOR PRECEDENCE =====")
print("2 + 3 * 4 =", 2 + 3 * 4)    # 14
print("(2 + 3) * 4 =", (2 + 3) * 4) # 20

# --------------------------------------------------------

print("\n===== 10. OPERATOR OVERLOADING =====")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # Overload ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # For printing objects
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 1)
p3 = p1 + p2

print("p1 + p2 →", p3)
print("p1 == p2 →", p1 == p2)
print("p1 == Point(2,3) →", p1 == Point(2,3))

# ========================================================
print("\n===== END OF ALL OPERATORS DEMO =====")

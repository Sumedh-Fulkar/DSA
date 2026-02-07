# ARITHMETIC OPERATOR
# Variables
a = 15
b = 4

print("ARITHMETIC OPERATORS")
# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

# COMPARISON / RELATIONAL OPERATOR
a = 13
b = 33

print("\nCOMPARISON/RELATIONAL OPERATORS")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# LOGICAL OPERATOR
a = True
b = False
print("\nLOGICAL OPERATORS")
print(a and b)
print(a or b)
print(not a)

# BITWISE OPERATORS
a = 10
b = 4

print("BITWISE OPERATOR")
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# ASSIGNMENT OPERATOR
a = 10
b = a
print("\nASSIGNMENT OPERATOR")
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# IDENTITY OPERATOR
a = 10
b = 20
c = a

print("\nIDENTITY OPERATOR")
print(a is not b)
print(a is c)

# MEMBERSHIP OPERATOR
x = 24
y = 20
list = [10, 20, 30, 40, 50]

print("\nMEMBERSHIP OPERATOR")
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# TERNARY OPERATOR
a, b = 10, 20
min = a if a < b else b

print("\nTERNARY OPERATOR")
print(min)
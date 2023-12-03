# Variable declaration and assignment
x = 5      # Integer
name = "John"  # String
pi = 3.14  # Float

# print() function is often used to output variables.

print(name) #o/p John
# We can get the data type of a variable with the type() function.
print(type(x)) # o/p <class 'int'>
print(type(name)) # o/p <class 'str'>
print(type(pi)) # o.p <class 'float'>

x = x + 1  # Reassigning x with a new value
# Variable names are case-sensitive.
X="ritik"
print(x) # o/p 6
print(X) # o/p ritik

a, b, c = 1, 2, 3 # We can assign values to multiple variables in a single line.
print(a,b,c) #o/p  1 2 3
print(a + b + c) #o/p  6





#We want to specify the data type of a variable, this can be done with casting
c = float(3)  
print(c); # o/p 3.0

# ------------------------
# if = 15;  invalid
# -------------------------
# Snake Case
user_name = "John"
total_amount = 1000

# Camel Case
calculateTotalAmount = str(1500)
myFunctionName = "Your Amount is :"
print(myFunctionName + calculateTotalAmount)

# Constants (using uppercase)
PI = 3.14159
GRAVITY = 9.8
MAX_SPEED = 300

# These values are considered constants,but it is changable and it is a convention not to change them. 



# -----------------------------------------------------
# -------------------------OUTPUT----------------------
# John
# <class 'int'>
# <class 'str'>
# <class 'float'>
# 6
# ritik
# 1 2 3
# 6
# 3.0
# Your Amount is :1500
# -----------------------------------------------------



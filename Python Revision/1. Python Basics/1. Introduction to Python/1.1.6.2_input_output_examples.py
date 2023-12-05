# 1. Reading input without a prompt
unprompted_input = input()
print("You entered:", unprompted_input)


# 2. Basic input and output
name = input("Enter your name: ")
print("Hello, " + name + "!")


# 3. Output with formatting
amount = 150.75
discount = 20
final_amount = amount - (amount * discount / 100)
print(f"The final amount after a {discount}% discount is: ${final_amount:.2f}")


# 4. Input and output with different data types
age = int(input(" Enter your age: "))
age1 = input("Conform your Enter your age: ")
print("You will be " + str(age + 10) + " in 10 years.")
print("\n")

# 5. Printing multiple values
print("For Dev refrence")
print('age',type(age))
print('age1',type(age1))
print("\n")
print("enter any key to make 4 Line space ")
input()


# 6. Using sep to change the separator
print("One", "Two", "Three","Four","Lets Make Four Line space", sep="-")
print("\n")
print("\n")
print("\n")
print("\n")


# 7. Using end to change the end character
print("This is on the same line", end=" ")
print("as the previous line.")
# 8. Taking multiple inputs using split()
a, b = input("Enter two values separated by a space: ").split()
print("\n")

# 9. Taking multiple float inputs
height, weight = map(float, input("Enter your height (in meters) and weight (in kilograms) separated by a space: ").split())

# 10. Displaying output using {} and .format()
txt = "your height is {}, your weight  is {}".format(height,weight)
print(txt)

# output
# Hi
# You entered: Hi
# Enter your name: Ritik
# Hello, Ritik!
# The final amount after a 20% discount is: $120.60
#  Enter your age: 23
# Conform your Enter your age: 23
# You will be 33 in 10 years.


# For Dev refrence
# age <class 'int'>
# age1 <class 'str'>


# enter any key to make 4 Line space

# One-Two-Three-Four-Lets Make Four Line space








# This is on the same line as the previous line.
# Enter two values separated by a space: 23 34


# Enter your height (in meters) and weight (in kilograms) separated by a space: 1.6 54
# your height is 1.6, your weight  is 54.0
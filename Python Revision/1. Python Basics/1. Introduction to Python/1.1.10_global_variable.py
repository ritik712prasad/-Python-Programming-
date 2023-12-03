# Global variable
global_variable = 10

def example_function():
    # Accessing the global variable
    #print("Inside the function - Global variable:", global_variable)
    # we can;t acces global_variable without using global keyword
    # Creating a local variable with the same name
    local_variable = 5
    print("Inside the function - Local variable:", local_variable)

    # Modifying the global variable with the 'global' keyword
    global global_variable
    print("Initially Global variable Declared with Value: ", global_variable)
    global_variable = 20
    print("Inside the function - Modified Global variable:", global_variable)

# Calling the function
example_function()

# Accessing the global variable outside the function
print("Outside the function - Global variable:", global_variable)


# OUTPUT

# Inside the function - Local variable: 5
# Initially Global variable Declared with Value:  10
# Inside the function - Modified Global variable: 20
# Outside the function - Global variable: 20
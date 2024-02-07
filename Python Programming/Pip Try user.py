# What is pip 
# Pip is a packages or modules if you like
# What is package : 
# A package contain all the files you need for a module
# Module are python code libraries you can include in your project

# In VScode open the folder where do you want to install package Go to terminal and open the new file 
# Then install your package example (Pip install Django)

# Then the package is installed sucessfully so we can use it

# Uninstall package : pip uninstall (package name)

# List package : To know what are the packages are installed use list command (pip list)

# Try Except 

# The try block lets you test a block of code for error
# The except block lets you handle the error
# The else block lets you execute code when there is no error 
# The finally block lets you execute code, regardless of the result of the try- and except bloxks

# Execption Handiling 
# When An error occurs, python will normally stop and generate an error message
# These exceptions can be handled using the try statment:

try:
    print(x)
except:
    print("An exception occured")

# Since the try block raises an error, the except block will be executed
    
# Else 

# You can use the else keyword to define a block of code to be executed if no errors were raised

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally 
    
# The finally block, if specified, will be executed regardless if the try block raises an error or not
    
''' try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
'''
# Raise an exception
    
# As a python developer you can choose to throw an exception if a condition occurs
# To throw an exception, use the raise keyword
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# User Input 
# Python allows for user input
# That means we are able to ask the  user for input

username = input("enter username")
print("Username is: " + username)



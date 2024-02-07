# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Example len() is python function that can be used on different object is the len() function


# Class polymorphism

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# Inheritance calss we can use the same polymorphism 

#=====END======


# Python Scope

# A variable is only available from inside the region it is created. This is called Scope

# Local Scope
# A variable created inside a function belongs to the local scope of that function and can only be used inside that function

def myfun():
    x = 100
    print(x)

myfun()

# Function inside Function
# As explained in the example above the variable x is not availbale outside function, but it is available for any function inside the function

def myfun():
    x = 300
    def myinnerfun():
        print(x)
    myinnerfun()

myfun()

# Global Scope
# A variable created in the main body of the python code is a global variable and belongs to the global scope
# Global variable are availbale from within any scope global and scope

y = 400

def myfunc():
    print(y)

myfunc()

print(y)

# Naming variable
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, One available in the global scope
# And one availbale in local scope

z = 500
def fun():
    z = 200
    print(z)
fun()

print(z)

# Global Keyword 
# We need to create global variable, but are stuck in the local scope you can use the global keyword

def ction():
    global a
    a = 600

ction()

print(a)


# =======END===========
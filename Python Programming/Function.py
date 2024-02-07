# Function  is a block of code which only runs whent it is called
# you can pass data known as parameters into a function
# A function can return data as result

# CREATING A FUNCTION
# In a python a function is defined using a def keyword

def function():
    print("Hello from function")

# calling a function 
# to call a function use the function name followed by parenthesis

def function():
    print("hello from a function")

function()

# there are two types of function:
# 1 built in function 
# 2 user defined function

# 1 built in function These function are defined and pre coded in python some examples of built in function are as follow
# min() max() len() sum() type() range() dict() tuple() set() print()

# user defined function:
# we can create functions to perform specific tasks as per our needs such function are called user defined function

# Function Arguments 
# there are four types of arguments that we can provide in a function
# Default 
# Keyword
# Required 
# Variable length

# DEFAULT We can provide a default value while creating a function this way the function assumes a default value even if a value is not
# provided in the function call for that argument

def name(a, b = "AB", c = "Doosa"):
    print("Hello,", a, b, c)

name("AMY") 

# Keyword:
# We can provide arguments with key = value this way the interpreter recogonizes the args by the parameter name hence the order in which the arguments are passed doesnot matter

def n(e, f, g):
    print("Hello,", e, f, g)

n(f = "D", g = "h", e = "A")

# Required 
# In case we don't pass the arguments with a key = value syntax then it is necessary to pass the args in the correct positional order and the args pass should match with actual function definition
# When numbers of arguments passed doesn't match to the actual function definition we get a type error

def E(fname, mname, lname):
    print("Hello,", fname, mname, lname)

E("peter", "Ego", "Quill")

# Variable length arguments:
# Sometimes we may need to pass more arguments than those defined in th actual function this can be done by this

# Arbitrary 
# While creating a function pass a * before the parameter name while defining the function The fun accesses the args by processing them in form of tuple

def nam(*name):
    print("Hello,", name[0], name[1], name[2])

nam("Aravind", "Doosa", "Netha")

# Key word arbitrary:
# While creating a fun pass a ** before the parameter name while defining the func.The func accesses the args by processing them in the form of dictionary

def M(**cls):
    print("hello,", cls["lname"], cls["jname"], cls["kname"])

M(jname = "Buchanan", kname = "Barnes", lname = "james")


# return Statement
# The return statement is used to return the value of the expression back to main function

def Chil(kname, sname, hname):
    return "Hello," + kname + " " + sname + " " + hname

print(Chil("Siri", "Rakhe", "Konda"))


# python recursion
# We can let the function call itsself such a process is known as calling a function recursively python

def fac(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * fac(num - 1))
    
num = 7;
print("number: ",num)
print("Fac: ",fac(num))

#=======END=============


# Python Module:
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application

# Creating a module
# To create a module just save the code you want in a file with the file extension .py:

def greeting(name):
    print("Hello, " + name)


# Use Module
# Now we can use the module we just created by using the import statement:
    
import pythonProject.module as module

module.greeting("Aravind")

# Variables in  module:

# The module can contain functions, as described, but also variables of all types

person1 = {
    "name" : "Aravind",
    "age" : 22,
    "country" : "India"
}

import pythonProject.module as module

a = module.person1["age"]
print(a)

# Naming a module
# We can name the module file whatever you like, but it must have the file extension .py
# Renaming a module
# you can create an allias when you import a module, by using the as keyword:

import pythonProject.module as m

a = m.person1["country"]
print(a)

# Built in module
# There are several built in module in python, Which you can import whenever you like

import platform

x = platform.system()
print(x)

# Using the dir() function 
# There is a built in dunction to list all the function names in a module.

import platform

x = dir(platform)
print(x)

# Import from module

# you can choose to import only parts from a module by using from keyword

from pythonProject.module import person1

print (person1["name"])

# Python Dates 
# A date in python is not a data type of its own, but we can import a module named datetime to work with dates as date objects

import datetime
y = datetime.datetime.now()
print(y)

# Date output 
# The datetime module has many methods to return information about the date object

import datetime
z = datetime.datetime.now()

print(z.year)
print(z.strftime("%A"))

# Creating Date objects
# To create a date, We can use the datetime() class (constructor) of the datetime module

# The datetime() class require three parameters to create a date: year, month, day

import datetime
p = datetime.datetime(2024, 1, 25)
print(p)

# The strftime() Method

#The datetime object has a method for formatiing date objects into readable string

import datetime

q = datetime.datetime(2001, 2, 1)
print(q.strftime("%B"))

# Python Math
# Python has a set of built in math functions, including an extensive math module, that allows you to perform mathematical tasks on number

# Built in math min() and max() these functions are to find the lowest or highest value in an iterable

w = min(7, 24, 53)
m = max(4, 8, 2)
print(w)
print(m)

# the abs function return the absolute + value of the specified number 

v = abs(-4.56)
print(v)

# The pow(x, y) function return the values of x to the power of y(x)

b = pow(5, 3)
print(b)

# The Math module

# python has also built in module called math, Which extends the list of mathematical functions

# math.sqrt return the suare root of a number

import math

c = math.sqrt(81)
print(c)

# The math.ceil() method round a number upwards to its nearest integer and the math.floor() method rounds a number downwards to its nearest integer and return result

import math

r = math.ceil(5.6)
f = math.floor(1.4)

print(r)
print(f)

#======Math module coming=====
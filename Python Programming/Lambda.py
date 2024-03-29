# Python Lambda
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments but can only have one expression

#Syntax
# lambda arguments : expression

# Add 10 to argument a, and return the result

x = lambda a : a + 10
print(x(5))

# lambda function can take any number of arguments

x = lambda a, b : a * b
print(x(5, 6))

# Why we use lambda function
# The power of lambda is better shown when you use them as an anonymous function inside another function
# Say you have a function definition that takes one arguments and that arguments will be multiplied with an unknown number

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#=========END===========

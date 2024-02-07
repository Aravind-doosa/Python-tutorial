# Python operators are used to perform operation values on variables and values
# Python divides the operators in the following groups:
# Arithmetic operators
# These are used with numeric values to perform common mathematical operations:
# Addition, Subtraction, Multiplication (*), Division (/), Modulus (%), Exponential (**), Floor division (//)

# Assignment Operator
# Assignment operators are used to assign values to variables

# =
x = 5
print(x)

# +=
x = 5
x += 3
print(x)

# -=

x -= 2
print(x)

# *=
y = 2
y *= 5
print(y)

# /=
y /= 2
print(y)

# %=
z = 5
z %= 3
print(z)

# //=
E = 5
E //= 3
print(E)

# **=
F = 5
F **= 3
print(F)

# &=
G = 5
G &= 3
print(G)

# |=

H = 5
H |= 3
print(H)

# ^=

i = 2
i ^= 3
print(i)

# >>=

j = 5
j >>= 3
print(j)

# <<=

K = 5
K <<= 3
print(K)

# Comparison operator

# == Equal to
# != Not Equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to

# Logical operator

# 'and' Operator return true if both statements are true
x = 5
print(x > 3 and x < 10)

# returns true because both the conditions are satisfied

# 'or' returns true if one of the statements is true
p = 10
print(p > 5 or p < 4)
# return false because the 1st statement is satisfied

# 'not' reverse the result returns false if the result true
o = 5
print(not (o > 3 and o < 10))
# returns reverse the result

# Identity operator
# identity operators are used to compare the objects, not if they are equal, but if they are actually the same objects
# with the same memory location

# 'is' return true if both variables are same object

AR = ["Apple", "Banana"]
NA = ["Apple", "Banana"]
RA = AR
AS = RA

print(AR is RA)
# returns True because z is the same object as x
print(AR is NA)
# returns False because x is not the same object as y, even if they have the same content
print(AS is AR)
print(AR == NA)
# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y
print(AR is not RA)
# returns False because z is the same object as x
print(AR is not NA)
# returns True because x is not the same object as y, even if they have the same content
print(AR != NA)
# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y

# Membership operator
# Membership operators are used to test if a sequence is presented in an object

# 'in' returns true if a sequence with the specified value is present in the object
E = ["Apps", "features"]
print("Apps" in E)
print("games" in E)

# Bitwise operators are used to compare binary numbers:

print(6 & 3)

print(6 | 3)

print(6 ^ 3)

print( ~3 )

print(3 << 2)

print(8 >> 2)

# END
# python supports the usual logical conditions from mathematics
# ==, !=, <, >, <=, >=

# if satatement is written by using if key word

a = 33
b = 50
if b > a :
    print("b is greater then a")

# Elif this key word in python sayong that if the above condition is not true try this condition

c = 40
d = 40
if d > c :
    print("d is greater then c")
elif d == c:
    print("both are equal")

# else this catches anything which is not caught by preceding condition

e = 200
f = 150
if f > e :
    print("f is great")
elif f == e :
    print("both are equal")
else :
    print("Yes idiot")

# Short hand if:
# if you have only one statement to excute you can put it on the same line as if statement
    
g = 100
h = 50
if g > h : print("g is grater than h")

# Short hand if else
# if you have only one statement to execute one for if and one for else you can put in same line

i = 2
j = 4
print("A") if i > j else print("B")

# And the and key word is a logical operator and is used to combine conditional statements

k = 100
L = 50
M = 200
if k > L and M > k:
    print("Both conditions are true")

# OR the key word or is a logical operator or is used to combine conditional statements
    
N = 4
O = 2
P = 5
if N > O or N > P:
    print("atleast one is true")

# NOT key word is a logical operator and is used to reverse the result of the condition 
    
Q = 7
R = 8
if not Q > R:
    print("Q is Not grster")

# Nested if
# you can have if statements inside if statement this is called nested if statement

X = 30
if X > 10:
    print("above 10")
    if X > 20:
        print("above 20!")
    else:
        print("but not above than 20")


# THE PASS SATATEMENT
# if cannot be empty but if you for some reason have an if statement with no content put in the pass statement to avoid error

S = 20
T = 40
if T > S:
    pass

#=========END========================
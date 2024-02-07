# Python while loops
# python loops: Python has two primitive loop commands
# while loops 
# for loops

# while loop : We can execute a set of statements as long as a condition is true

# Example :
i = 1
while i < 6:
    print(i)
    i += 1

# the while loop require relevant variables to be ready in this example we need to define an indexing variable, i, which we set to 1

# The Break statement
# with the break statement we can stop the loop even if the while condition is true

# Example
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1

# The continue statement
# With the continue statement we can stop the current iteration and continue with next
# Example
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# The else statement
# with the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("is no longer less than 6")


# LOOPS FOR Python
# For loops : A for loop is used for iterating over a sequence (that is either a list a tuple a dictionary a set or a string)
# this is less like the for keyword in other programming language and work more loke an iterator method as found in other object oriented programming language
    
fruits = ["apple", "banana", "cherry"]
for x in fruits :
    print(x)

# looping through a string
# even strings are iterable objects they contain a sequence of character

for x in "banana":
    print(x)

# the break statement
# with the break statement we can stop the loop before it has looped through all the items

a = ["one", "two", "three"]
for x in a:
    print(x)
    if x == "two":
        break
# the continue statement
# with continue statement we can stop iteration of the loop and continue with the next

b = ["four", "five", "six"]
for x in b:
    if x == "five":
        continue
    print(x)

#the range function
# to loop through a set of code a specified number of times we can use range function
# the range() function returns a sequence of numbers starting from 0 by default and increments by 1 and end at a specified number

for x in range(6):
    print(x)
    
# Range function default to 0 as a starting value however it is possible to specify the staring value by adding a parameter 

for x in range(2, 6):
    print(x)

for x in range (2, 30, 3):
    print(x)

# Else in for loop  
# the else keyword in a for loop specifies a block of code to be executed when the loop is finished
    
for x in range(6):
    print(x)
else:
    print("finished")

# Nested loop 
# a nested loop is a loop inside a loop
# the inner loop will be executed one time for each iteration of the outer loop
    
d = ["a", "b", "c"]
e = ["d", "e", "f"]

for x in d:
    for y in e:
        print(x, y)

    
# the pass statements
# for loops cannot be empty but if you for some reason have a for loop with no content, put in the pass statement to avoid getting error

for x in [0, 1, 2]:

 pass


#==================END=======================
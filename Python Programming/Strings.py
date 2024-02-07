# Strings in python anything that you enclose between single and double quotation mark is string

# String example
name = "Samuel"
print("Hello," + name)

# String
print("He Said, \"I want to eat an apple\".")

# Multiple string
recipe = """
1. Heat the pan and add oil
2. Crack the egg
3. Add salt in egg and mix well
4. Pour the mixture in pan 
5. Fry on medium heat 
"""
print(recipe)

note = '''
This is a multiline string
It is used to display multiline message in the program 
'''
print(note)

# Length of string We can find a length of a string using len() function
Fruit = "Mango"
len1 = len(Fruit)
print("Mango is a", len1, "letter word")

# String as an Array
# Like many other popular programming languages, strings in python are arrays of bytes
# representing unicode character

a = "Hello World!"
print(a[1])

# Looping through a string
# since strings are array we can loop through the characters in a string with for loop

for x in "banana":
    print(x)

# Check String = we can check if certain character is present in a string by "in" keyword

txt = "The best thing in world is mothers lap"
print("mother" in txt)
print("mother" not in txt)
if "lap" in txt:
    print("yes, 'lap' is present")

# slicing : You can return a range of character by using the slice syntax

b = "Super ra"
print(b[1:6])

# slice from start
print(b[:2])

# slice from end
print(b[1:])

# Negative Indexing

print(b[-5:-2])

# Upper case in slicing
a = "welcome"
print(a.upper())
print(a.lower())

# strip() removes the white spaces

c = " Good morning "
print(c)
print(c.strip())

# Replace the string with another
d = "Evening"
print(d.replace("E", 'D'))

# Split() it split the string
E = "Whats, up"
print(E.split(","))

# Concatenation
a = "hi"
b = "how are you"
c = a + b
print(c)
d = a + " " + b
print(d)

# String format we can combine numbers and string through format() method

age = 35
txt = "my name is Hari, and i am {}"
print(txt.format(age))

# We can use index numbers to place the numbers in correct placeholders
Quantity = 3
item = 456
price = 50.05
order = "I want to pay {2} dollars for {0} piece of items {1}"
print(order.format(Quantity, item, price))

# Escape character to insert character that are illegal in a string
# An Escape character is a backslash \ followed by the character you want to insert
txt = "We are the so called \"vikings\" from north"
print(txt)

# Boolean Values in Python
# In programming you often need to know if an expression is True or False
# When you compare two values, the expression is evaluated and Python returns the boolean values
print(bool(0))

a = 200
b = 159

if b > a:
    print("b is greater than a")
else:
    print("b is less than a")

# END

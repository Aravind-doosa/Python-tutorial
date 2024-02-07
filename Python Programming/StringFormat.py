# String formating
# To make sure a string will display as expected, We can format the result with the format method

# The format() method allows you to format selected parts of a string
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or userinput

# To Control such values, add placeholders {} in the text, and run through the format() method:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Multiple values 

# If you wnat use more values, just add more values to the format method

quantity = 3
i = 567
p = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, i, p))

# Index numbers we can also use the format mwthod by using the index numbers

# Named Indexes
# We can also use named indexes by entering a name the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "ford")

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "ford", model = "mustang"))

# ======END=======
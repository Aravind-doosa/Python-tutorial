# Lists are ordered collection of data items.They store multiple items in a single variable
# list items are separated by Commas and enclosed with in square brackets.This can be
# changeable meaning we can alter them after creation
Lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = ["red", "blue", "green", "yellow"]
print(Lst1)
print(lst2)

# List indexes: Each item in a list has its own unique index it can be used to access any item from the list
colors = ["red", "blue", "green", "yellow"]

# Accessing list items: Positive indexing
print(colors[2])
print(colors[1])

# Negative Indexing:
print(colors[-1])
print(colors[-4])

# if condition
if "red" in colors:
    print("Red is present")
else:
    print("Red is not absent")
# check for item:
if "orange" in colors:
    print("Orange is present")
else:
    print("Orange is absent")

# Range index
Language = ["Python", "Java", "C", "C++", "JavaScript", "Html"]
print(Language[1:4])
print(Language[-4:-1])
print(Language[1:])
print(Language[-4:])
print(Language[:3])
print(Language[:-2])

# Alternate list
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		# using positive indexes
print(animals[-8:-1:2]) 	# using negative indexes

# Third Consecutive within given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

# adding items in list
# Append(): This method appends item to the end of the existing list
# Syntax of append is paint.append("red")
Paint = ["red"]
print(Paint)

# Insert(): In this method we can insert item at given index
Size = ["xs", "M", "L"]
Size.insert(1, "S")
print(Size)

# Extend():In this method it adds an entire list or any other collection Data types to Existing
# List + List
A = ["one", "two", "three"]
B = ["four", "five", "six"]
A.extend(B)
print(A)

# List + Set
C = ["Arya", "Bun", "Des"]
D = {"N", "vp", "Push"}
C.extend(D)
print(C)

# List + Tuple
E = ["leo", "kahle"]
F = ("Beast", "Jailer")
E.extend(F)
print(E)

# List + Dict
G = ["ghi", "jkl"]
H = {"ar": 23, "rp": 26}
G.extend(H)
print(G)

# Concatenate List
i = ["Super", "indigo"]
J = ["Jack", "Jill"]
print(i + J)

# Removing a item in list
# pop(): In this method it removes the last item from list if there is no index provided
i = ["Super", "indigo"]
i.pop(0)
print(i)
J = ["Jack", "Jill"]
J.pop()
print(J)

# Remove it removes a specific item
F = ["Super", "indigo"]
F.remove("Super")
print(F)

# Del it is not a method it is a key word delete a specific item from list
Colors = ["red", "blue", "green"]
del Colors[2]
print(Colors)

# Clear in this method it clears all items and print empty list
Paint = ["red", "blue", "green"]
Paint.clear()
print(Paint)

# Changing list items.We should just specify the index where we want to change the list
Paint = ["red", "blue", "green"]
Paint[2] = "orange"
print(Paint)

# We can change more than a single item at once by specifying the index range
Animals = ["cat", "dog", "bat", "Ant"]
Animals[1:2] = ["Tiger", "Lion"]
print(Animals)

# List Comprehension are used for creating a new list from iterables[list,tuples.dict.set,array and strings]
# Syntax: list = [expression(item)for item in iterable if condition]
Animals = ["cat", "dog", "bat", "ant"]
Animals_a = [item for item in Animals if "a" in item]
print(Animals_a)
Animals_a = [item for item in Animals if (len(item) > 2)]
print(Animals_a)

# Method in list
# sort(): This is method sorts list in ascending order
colors = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

# Reverse it just reverse the list
B = ["red", "blue", "green"]
B.reverse()
print(B)

# index() this method returns the index of first Occur of the list item
Size = [10, 20, 30, 40, 50]
print(Size.index(20))

# Count(): Returns the count of the number of items with the given values
num = [9, 2, 7, 3, 2, 5, 2, 6, 7, 9, 2, 1]
print(num.count(2))

# Copy() returns copy of the list this can be done to perform operations on the list without modifying the original
num = [9, 2, 7, 3, 2, 5, 2, 6, 7]
new = num.copy()
print(num)
print(new)

# End

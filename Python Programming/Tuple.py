# Tuples: Tuples are ordered collection of data items.They store multiple item in a single variable. Tuple item are
# supported by commas and enclosed with in a round brackets.Tuples are unchange able meaning we can not alter them after creation

tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "blue")
print(tuple1)
print(tuple2)

# ordered : When we say that tuples are ordered, it means that the item have a order, and that order will not change
# unchangeable: Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created
# allow Duplicates : since tuples are indexed they can have items with same value

# we can insert all the data type in tuple

details = ("Aravind", 18, "python", 9.8)
print(details)

# indexes in tuple it started from 0 for 1st item second item has index 1 and followed by 2, 3, 4....
# Each item in a tuple has its own unique index. This can be used to access any particular item from the tuple
print(details[0])

# positive indexing As we can see that tuple items have index as such we can acess itens using these indexes

# negative indexing is Similar to positive, negative indexing is also used to acess items,but from end of the tuple
# the last item has index [-1], second last item has index[-2] and so on

print(details[-1])

# checking for a item We can check the givrn item is present in the tuple or not by using the key word

if 18 in details:
    print("18 is present")
else:
    print("18 is absent")

# range of index we can print a range of tuple item by specifying where do you want to start where do you want to end 
# and also we can jump the index
    
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat")
print(animals[0:5])
print(animals[-5:-2])
print(animals[4:]) #printing all element from a given index till the end
print(animals[-4:]) #by using negative index
print(animals[:6]) #printing all elements from start to a given index
print(animals[:-3]) #by negative index
print(animals[::2])#printing alternative index
print(animals[-7:-1:2])#using negative indexes
print(animals[1:7:3])#printing every 3rd consecutive withing given range

# Manipulating Tuples
#Tuples are immutable, hence if you want to add,remove or change tuple item,then first you must change tuple to list.
#then perform operation on that list and change to tuple

tup = ("super ra", "html", "css", "bootstrap", "ten")
temp = list(tup)
temp.append("three")   #add item
temp.pop(2)            #remove item
temp[2] = "Happy"      #change item
tup = tuple(temp)
print(tup)
 
# concatenate : we can directly concatenate two tuples with out converting them to list
Wholetuple = animals + tup
print(Wholetuple)

# unpacking Tuples it is a process of assigning the tuple items as values to variables
info = ("Ashish", 22, "css")
(name, age, group) = info
print("name:", name)
print("age:", age)
print("group:,", group)

# In above example we know that the numbers and variables are equal, But what if we have more numbers of item then the variables
# We can add * to one of the variables and depending upon the position of variables and number of python items,python matches variables to values and assign it to variables
fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

# -----------------END------------------
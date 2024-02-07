# python sets: Sets are unordered collection of data items.They store multiple items in a single variable.they are separeated by commas and enclosed within curly brackets{}
# Sets are unchangeable meaning you cannot change items of the set once created sets do not contain duplicate items

info = {"carla", 19, False, 5.9, 18}
print(info) # Here we see that items are occured in random order and hence they cannot be accessed using index numbers.Also sets do not allow duplicate value

#Accessing set items:

# Using a for loop: You can acess items of set using a for loop

for item in info:
    print(item)

# ADD items to set:
 # if you want to add a single item to the set use add()method
cities = {"HYD", "NZB", "KMR", "RR"}
cities.add("USA")
print(cities)

# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
cities2 = {"ind", "dich", "wht"}
cities.update(cities2)
print(cities)

#Difference between discard and remove if we remove an item that not present in set, then remove raise error() Wheras discard does not raise the error
Room = {"Ar", "RA", "CH", "NA"}
Room.remove("CH")
print(Room)
Room.discard("KI")
print(Room)

# There are various other methods to remove items from the 
# SET: pop(), del(), clear()
# Pop(): In this method removes a last item but we don't know which item is get popped because the set is unordered 
# We can acess the popped item if you assign the pop method to a variable

Mov = {"GK", "HM", "SA", "NS", "AA"}
sep = Mov.pop()
print(Mov)
print(sep)

# Del it is not a method it is a key word which deletes the set entirely
'''
JAN = {"py", "JS", "C", "HT"}
del JAN
print(JAN)
'''

# CLear this method clear all items in the set and print a empty set
FEB = {"WHT", "FT", "GY", "MI"}
FEB.clear()
print(FEB)

# JOIN SETS
# Set in python more or less work in the same way as sets in mathematics.We can perform operations like union and insertion on the sets just like mathematics

# union() and update()
# The union and update methods print all the items that are present in set .The union method returns a new set Whereas update adds item into existing set from another

#EXAMPLE UNION

What = {"Dh", "AP", "SK", "AN"}
KARVAD = {"MM", "DD", "BB"}
VIP = What.union(KARVAD)
print(VIP)

# UPDATE
What.update(KARVAD)
print(What)

# Intersection and intersection update
# intersection and intersection update methods print only item that are similar to the both sets The intersection returns a new set whereas the interscetion update into the existing 
frds = {"AR", "RK", "AS", "Su", "SA"}
frds1 = {"AR", "Su", "MD", "RA"}
frds2 = frds.intersection(frds1)
print(frds2)

# intersection update 
frds.intersection_update(frds1)
print(frds)

# Symmetric_difference and Symmetric_difference_update
# These method print only items that are not similar to the both the sets.Symmetric difference returns a new set whereas symmetrixc difference update return in existing set

frds4 = frds.symmetric_difference(frds1)
print(frds4)

# symmetric_difference update 
frds.symmetric_difference_update(frds1)
print(frds)

# difference() and difference update()
# In this methods print only items that are only present in original set and not in both.and the difference b/w the two is same as above methods
Sec = {"A", "B", "C", "D"}
Sec1 = {"B", "D", "E", "F", "G"}
frd6 = Sec.difference(Sec1)
print(frd6)

# difference_update
print(Sec.difference(Sec1))

# Set Methods
# Apart form the methods we discussed earlier in the chapter there are some more methods that we can use to manipulate sets

# If we wanr to check if items of a particular set are present in another set

#isdisjoint():
# This isdisjoint method checks if item of given set are present in another set this method return false if item are present else it return true

one = {"all", "some", "ana", "three"}
one1 = {"two", "whe", "some", "no"}
print(one.isdisjoint(one1))

one2 = {"m", "N", "O"}
print(one.isdisjoint(one2))

# issuperset():
# It checks if all item of a particular set are present in the original set it return true if all the items are present else it returns false
one3 = {"ana", "all"}
print(one.issuperset(one3))
# one false example
print(one.issuperset(one2))

# issubset():
# the issubset method checks is all the items of the original set are present in the particular set it returns true if present or false
He = {"k", "j", "M"}
She = {"k", "M"}
print(She.issubset(He))


#-------END---------

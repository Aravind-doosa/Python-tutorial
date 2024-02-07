# Dictionaries: Dict are ordered collection of data itens they store multiple items in a single variable separated by commas and enclosed with in curly braces

info = {'name':'Karan', 'age':19, 'eligible': True}
print(info)

#Accessing items
# Accessing single value: values in dict can be accessed by key words or by using get method
print(info['age'])
print(info.get('name'))

#Accessing multiple items we can print all values in dict values()method
print(info.values())

#Accessing keys: we can print all the keys in dictnusing key() method
print(info.keys())

#Accessing key values : we can access all key values in the dict using items
print(info.items())

#ADD/REMOVE items
# create a new key and assign a value to it
info['DOB'] = 2001
print(info)

#UPDATE in this method if we want to update a value we can use the same old key word if we want to create a  new we should write a new key word
info.update({'age':23})  #Here the age will be updated to 23
info.update({'G':55}) #Here it will add a new key word
print(info)

#REMOVE

#clear(): it clear the whole items from dict
'''
info.clear()
print(info)
'''
print(info)

#pop it will remove the specific item that you mentioned in parameter

info.pop('eligible')
print(info)

# POP item it removes the last item in the list
info.popitem()
print(info)

# DEL in this method we can delete specific key by using key word in del method
# if we not mentioned any key in del it will del all the list

del info['age'] #Delete the age from the list
print(info)
'''
del info # delete all the list
print(info)
'''

# COPY DICT
# In this method we can copy all the content from one dict to another 

newinfo = info.copy()
print(newinfo)

# or we can use the dict() to make a new dict with the items of original dict

Secoinfo = dict(newinfo)
print(Secoinfo)


#==========END============
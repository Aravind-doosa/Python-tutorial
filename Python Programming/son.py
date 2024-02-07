# Json in python 

# JSON Stands for javascript Object Notation it is a built in package provided in python that is used to store and exchange data

# JSOn to python

import json

colors = '["RED", "Yellow", "Green", "Blue"]'

list1 = json.loads(colors)
print(list1)

# Converting pyhton to json string

import json 

list2 = ['Red', 'yellow', 'green', 'blue']

jsonobj = json.dumps(list2)
print(jsonobj)

# We can convert python objects of the following types into json strings:
# dict      object
# list      Array
# tuple     Array
# string    String
# int       number
# float     number
# true      true
# false     false
# none      null


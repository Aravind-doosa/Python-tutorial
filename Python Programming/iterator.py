# Python iterator 
# Pyrhon iterator is an object that contain countable number of values 
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
# technically in python an iterator is an object which implements the iterator protocol which consisit of the methods __iter__() and __next__()

# Iterator vs Iterable

# Lists, tuples, dictionaries, Sets and String are all iterable objects. They are iterable containers which you can get an iterator from
# All these objects have a iter() method which is used to get an iterator:

b = ("apple", "banana", "cherry")
myit = iter(b)

print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator 
# We can also use a for loop to iterate through an iterable object

a = ("dog")

for x in a:
    print(x)


# To create an iterator 
    
# To create an object class as an iterator you have to implementthe methods __iter__() and __next() to your object
# As we know all classes have a function called __init__() Which allows you to do some initializing when the object is being created
# The __iter__() method acts similar you can do operartions but must always return the iterator object itself
# The __next__() method also allows you to do operation and must return the next item in the sequence
    
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Stop iteration 
# The example above would be continue forever if you had enough next() statments or if it was used in a for loop

# To prevent the iteration from going on forever we can use the stopiteration statment
# In the next method we can add a terminating condition to raise an error if the iteration is done a specified number of times

class MyNumbers:
   def __iter__(self):
      self.a = 1
      return self
   def __next__(self):
      if self.a <= 20:
         x = self.a
         self.a += 1
         return x
      else:
         raise StopIteration
      
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
   print(x)
      


#========END=======

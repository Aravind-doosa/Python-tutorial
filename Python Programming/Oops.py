# Python oops
# A class is a blueprint or a template for creating object while an object is an insatance or a copy of the class with actual values

# Creating a class
# Create a class using the class keyword

class Details:
    name = "Simran"
    age = 20
    
obj1 = Details()
print(obj1.name)
print(obj1.age)

# Self method 
# The Self parameter is a reference to the current instance of the class and is used to access variable that belong to class
# It must be provided as the extra parameter inside the method definition 

class Details:
    name = "simran"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()

# __init__ method :
# The __init__ method is used to initialize the object's state and contains statments that are executed at the time of object creation

#EXAMPLE
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("crab", "Crustaceans")
print(obj1.animal, "belohgs to the", obj1.group, "group.")

# We can also modify and delete objects and their properties:

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("crab", "crustaceans")
obj1.animal = "Shrimp"
print(obj1.animal, "belongs to the", obj1.group, "group.")

# Delete objects and properties

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("crab", "Crustaceans")
del obj1
print(obj1.animal, "belohgs to the", obj1.group, "group.")

#==============END==================

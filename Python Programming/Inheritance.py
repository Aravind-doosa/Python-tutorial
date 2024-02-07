# Python Inhertiance 

# Inheritance allows us to definr a class that inherits all the methods and properties from another class
# Parent Class is the class being inherited from also called base class
# Child Class is the class that inherits from another class also called derived class


# Creating a parent class
# Any class can be a parent class So the syntax is the same as creating any other class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person ("John", "Doe")
x.printname()

# Creating a childclass

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class College:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(College):
    pass

y = Student("Aravind", "Doosa")
y.printname()

# Add __init__()
# So far we have created a child class that inheits the properties and method from its parent

# we want to add the __init__() function to the child class (instead pass keyword)
# When we add __init__() function, the child class will no longer inherits the parent's __init__() function
# So to keep the inheritance of the parent's class __init__() function, add a call to the parent's __init__ function:


class school:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(school):
    def __init__(self, fname, lname):
        school.__init__(self, fname, lname)

z = Student("Aravind", "Doosa")
z.printname()

# we have sucessfully added the __init__ function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__ function

# Use the Super() Function

# Python also have a super function that will make the child class inherits all the methods and properties from the parent:

class Student(school):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


p = Student("Rakesh", "Siri")
p.printname()

# By using the super function you don't have to mention the parent class name it will automatically inherits the methods and properties from its parent


# ADD propeties 
# In below example the year 2019 should be a variable and passed into the student class when creating student object. to do so add another parameter in the __init__ fun

class school:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(school):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2022


p = Student("Rakesh", "Siri")
print(p.graduationyear)

# ADD Methods 
# ADDing a method called welcome to the student classs:

class school:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(school):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    
    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

r = Student("Ashish", "Raj", 2022)
r.welcome()

#====END=======
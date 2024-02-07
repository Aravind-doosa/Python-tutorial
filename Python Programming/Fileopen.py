# File Handling is an important part of any web application
# Python has several functions for creating, reading, updating, and deleting files.

# FILE HANDILING

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file.

# "r"- Read- Default value. Opens a file for reading, error if the file does not exist
# "a"- Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - opens a file for writing, create the file if it does not exist
# "x" - create - Creates the specified file, returns an error if the file exist
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode


# To Open a file for reading it is enough to specify the name of the file

f = open("demo.txt")


# The open() function returns a file object, When has a read() method for reading the content of the file

d = open("demo.txt", "r")
print(d.read())

# READ ONLY PARTS OF THE FILE 
# By default the read() method return the whole text, but you can also specify how many characters you want to return

c = open("demo.txt", "r")
print(c.read(4))

# READ LINES
# You can return one line by using the readline() method

e = open("demo.txt", "r")
print(e.readline())

# By Looping through the lines of the file, you can read the whole file, line by line:

g = open("demo.txt","r")
for x in g:
    print(x)


# Close Files 
# It is good practice to always close the file when you are done with it

h = open("demo.txt", "r")
print(h.readline())
h.close()


# PYTHON FILE WRITE

# WRITE TO AN EXISTING FILE
# TO write to an existing file, you must add a parameter to the open() function:

# "a" - Append - Will append to the end of the file
# "w" - Write - will over write any existing content 

i = open("demo2.txt", "a")
i.write("This content has been writing")
i.close()

# open and read the file after the appending

i = open("demo2.txt", "r")
print(i.read())

# "W"- Over write the content

k = open("demo3.txt", "w")
k.write("Woops! I have deleted the content!")
k.close()

# Open and read the file after the overwriting:
k = open("demo3.txt", "r")
print(k.read())


# CREATE A NEW FILE 

# To create a new file in python, Use the open() method, with one of the following parameter
# "r"- Create - will create - will create a file,return an error  if the fiel exist
# "a" - Append - Will create a file if the specified file doesnot exist
# "w"- Write - will create a file if the specified file does not exist

# o = open("myfile.txt", "x")


# Delete a file :
# To delete a file, you must import the os module, and run its os.remove() function:

import os 
os.remove("myfile.txt")

# Delete folder 
# To delete an entire folder, Use the os.rmdir() method

# import os
# os.rmdir("Foldername")


# ====== END ======

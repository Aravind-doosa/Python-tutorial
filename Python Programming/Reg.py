# Python regex or Regular Expression is a sequence of character that forms a search pattern

# RegEx can be used to check if a string contains the specified search pattern

# Python as a built in package called re, which can be used to work with regular expression

# RegEx in python 
# When you have imported the re module you can start using regular expression

import re

txt = "the rain in Spain"
x = re.search("^the.*Spain$", txt)

if x:
    print("Yes ! we have a match")
else:
    print("no match")

# RegEx functions 
# The re module offers a set of functions that allows us to search a string for a match

# findall   return a list containing all matches 
# Search    returns a match object if there is a match anywhere in the string
# Split     returns a list where the string has been split at each match
# Sub       Replaces one or many matches with a string
    


# METACHARACTERS

# Meta characters are characters with a speaial meaning:
    
'''
[]           a set of characters       "[a-m]"
\            signals a special seq     "\d"
.            any character             "he..o"
^            Start with                "^hello"
$            Ends with                 "hello$"
*            zero or more occurences   "he.*o"
+            one or more occurences    "he.+o"
?            Zero or one occurrences   "he.?o"
{}           Exactly the specifed num  "he.{2}o"
|            Either or                 "falls|stay"
()           capture and group'''

# SPECIAL SEQUENCES

# A special sequence is a \ followed by one of the character in the list below and has a special meaning

'''
\A     Returns a match if the specifed character are at the beginning of strung   "\Athe"
\b     returns a match where the specified character are at beginning or at end   r"\bain"
\B     returns a match where the specified charac are present but not at first or last  r"\Bain"
\d     returns a match where the string contains digits                           "\d"
\D     returns a match where the string doesnot contain digit      "\D"
\s     returns a match where the string  contain a white space chara       "\s" 
\S     returns a match where the string Doesnot contain white space character      "\S"
\w     returns a match where the string contain a to z any word character a to z digit from 0 to 9   "\w"
\W     returns a match where the string doesnot contain any word character             "\W"
\Z     return a match if the specifed characters are at the end of teh string       "spain\Z" '''

# SETS 
# A set is a set of character inside a pair of square brackets[] with a special meaning
'''
[arn]  	Returns a match where one of the specified characters (a, r, or n) is present
[a-n]	Returns a match for any lower case character, alphabetically between a and n
[^arn]	Returns a match for any character EXCEPT a, r, and n
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string'''


# FIND All function
# In this Function findall() function returns a list containing all matches 

import re

txt = "The rain in spain"
y = re.findall("ai", txt)
print(y)

# THE Serach() function

# The search() function searches the string for a match, and return a match object if there is a match
# If there is more than one match, only the first occurence of the match will be returned

import re
txt = "the rain in spain"
z = re.search("\s", txt)

print("The first while space char is located in position:", z.start())

# The Split() function 
# The split() function returns alist where the string has been split at each match:

import re
txt = "the rain in spain"
m = re.split("\s", txt)
print(m)


# The sub() function

# The sub() function replaces the matches with the text of your choice

import re
txt = "the rain in spain"
n = re.sub("\s", "9", txt)
print(n)

#You can control the number of replacements by specifying the count parameter:

k = re.sub("\s", "9", txt, 2)
print(k)


#MATCH OBJECT
#The Match object has properties and methods used to retrieve information about the search, and the result:

'''.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match'''
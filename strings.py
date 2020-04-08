# assigning string
name="john"
name='john'
name=str("john")

# immutable
str1 = "hello"
str2 = "hello"

print(id(str1)) 
print(id(str2)) 

str2 = str2 + "world"
print(id(str1))
print(id(str2))

str1 = "hello"

print(str1+"world")
print(str1*5)

string="welcome"
print(string[1:4])

"""ord() and chr()"""

print(ord('s'))
print(chr(115))

string="sridhar"
print(len(string))
print(max(string))
print(min(string))

""" membership operators"""

print("s" in string) 
print( "sri" not in string)

""" string comparison
==, >, <, !=, >=, <=
"""
s="sri"
a="sir"
print(s==a)
print(s!=a)
print(s<a)
print(s>a)
print(s<=a)
print(s>=a)

""" string iterative """

str1 = "sridhar"
for i in str1:
    print(str1)

"""  testing string"""

s="sridhar"

print(s.isalpha())
print(s.isalnum())
print(s.isspace())
print(s.isupper())
print(s.islower())
print(s.isdigit())
print(s.isidentifier())    

text="welcome to python"
print(text.endswith("on"))
print(text.startswith("on"))
print(text.count("o"))
print(text.find("o"))
print(text.rfind("o"))
print(text.find("onto"))

text1="my name is sridhar"
print(text1.capitalize())
print(text1.upper())
print(text1.lower())
print(text1.title())
print(text1.swapcase())
print(text1.replace("sridhar","blue"))




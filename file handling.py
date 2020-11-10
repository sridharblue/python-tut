'''
Python uses file objects to interact with external files on your computer. These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails, Excel documents, etc. Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily available. (We will cover downloading modules later on in the course).
Python has a built-in open function that allows us to open and play with basic file types. First we will need a file though. We're going to use some IPython magic to create a text file!
'''
#creating and writing a text file
file = open(r'D:\Repos\python-tut\file_handling.txt', "w")
file.write("Hello this a quick test file,\nthis is the second line\nthis is the third line\n")
file.close()

#opening and reading a test file
file = open(r'D:\Repos\python-tut\file_handling.txt', "r")
print(file.read())
file.close()

#readlines() method will return a list of each lines
file = open(r'D:\Repos\python-tut\file_handling.txt', "r")
print(file.readlines())
file.close()

#appending new lines using append method
file = open(r'D:\Repos\python-tut\file_handling.txt', "a")
file.write('this is the fourth line appended using append method\n')
file.close()

#reading the file in read mode
file = open(r'D:\Repos\python-tut\file_handling.txt', "r")
print(file.read())
file.close()

file = open(r'D:\Repos\python-tut\file_handling.txt', "r")
for line in file:
    print(line)
file.close()

#new method to open and close a file without close()
with open(r'D:\Repos\python-tut\file_handling.txt', "r") as file:
    contents = file.read()
    print(contents)


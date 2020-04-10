file = open("D:\demofile.txt", "w")
file.write("this is the first line\nthis is the second line\n")
file.close()

file=open("d:\demofile.txt","r")
print(file.read())
file.close()

file=open("d:\demofile.txt","a")
file.write("this is third line\n")
file.close()

file=open("d:\demofile.txt","r")
print(file.read())
file.close()

file=open("d:\demofile.txt","r")
for line in file:
    print(line)
file.close()


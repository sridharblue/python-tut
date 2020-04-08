list1=list()
print(list1)
list2=list([22,33,44])
print(list2)
list3=list(["tom","cat","dog"])
print(list3)
list4=list("22,33,44")
print(list4) 


print(list3[1])


print(list2+list3)
print(max(list3))
print(min(list3))
print(len(list3))
print("tom" in list3)
print("tom" not in list3)

for i in list3:
    print(list3)

###slicing###
print(list4[5:])

###traversing###
for i in list3:
    print(i, end="")

"""commonly used list functions
append()
extend()
count()
index()
sort()
pop()
insert()
remove()
reverse()
"""

sri=list([22,33,44,55,22,66])
sri.append(11)
print(sri)

print(sri.count(22))

sri.extend(list4)
print(sri)

print(sri.index(55)) ##returns index of 55 in the list sri=list([22,33,44,55,22,66])

sri.insert(2,'sri')
print(sri)

print(sri.pop(0))
print(sri)

sri.remove('sri')
print(sri)

sri.reverse()
print(sri)

sri1=list([1,5,9,4,2,7])
sri1.sort()
print(sri1)

"""   LIST COMPREHENSION"""

sri = [i for i in range(10)]
print(sri)
sri1= [i+1 for i in range(10)]
print(sri1)

sri2= [ i for i in range(10) if i%2==0 ]
print(sri2)


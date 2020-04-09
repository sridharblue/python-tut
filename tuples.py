""" Tuples are IMMUTABLE"""

t1=(11,22,33)
# t2=tuple("qwerty")
# t3=([11,'ww','rr',22])
# print(t1)
# print(t2)
# print(t3)

""" tuple function 
max()
min()
len()
sum()

"""
# print(len(t1))
# print(sum(t1))
# print(max(t1))
# print(min(t1))

for i in t1:
    print(i)


""" slicing """
sri=(34,57,87,35,90,78)
print(sri[0:2])
print(sri[4:])


print( 33 in sri)
print(34 in sri)
print(45 not in sri)
print( 90 not in sri)



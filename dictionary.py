friends={'tom': '111-222-333',
        'jerry': '999-888-777',}
print(friends)

"""retrieve, modify, add, del, """

print(friends['tom'])
friends['tom'] = '333-333-333'
print(friends)
friends['bob'] = '444-555-666'
print(friends)
del friends['tom']
print(friends)

test={'a':'aaa', 'b':'bbb', 'c':'ccc', 'd':'ddd'}
print(test)
for i in test:
    print(i , ":" , test[i])
print("the length of the dict is:" , len(test))

"""equality test ---- cant use <, >, <=, >="""

test1={'a':'111', 'b':'222'}
print(test==test1)
print(test!=test1)

""" Dictionary methods
popitem()
keys()
values()
clear()
get(key)
pop(key)
"""
print(test)
print(test.popitem())
print(test)

print(test.keys())
print(test.values())

print(test.get('a'))
print(test.get('d'))

print(test.pop('a'))
print(test)




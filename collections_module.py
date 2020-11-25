from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(lst))
print(Counter('aabsbsbsbhshhbbsbs'))

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print(Counter(words))

# Methods with Counter()
c = Counter(words)
c.most_common(2)

''' Common patterns when using the Counter() object
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts '''

#defaultdict
from collections import defaultdict
d = {}
d['one'] 

d  = defaultdict(object)
d['one'] #defaultdict will assign a default value to a key if its not present, in this case its a object type
for item in d:
    print(item)

d = defaultdict(lambda: 0) #default dict usally used in conjunction with a lambda
print(d['one'])
d['two'] = 2
d['three']

print(d)

#ordereddict

# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# d['e'] = 5
# d['f'] = 6
# d['g'] = 7
# d['h'] = 8
# d['i'] = 9
# d['j'] = 10

# print(d)

# for k,v in d.items():
#     print(k,v)

from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9
d['j'] = 10

print(d)

for k,v in d.items():
    print(k,v)

#checking boolean output
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3

# d1 = {}
# d1['a'] = 1
# d1['b'] = 2
# d1['c'] = 3

# print(d == d1) #this will be true

from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

d1 = OrderedDict()
d1['a'] = 1
d1['c'] = 3
d1['b'] = 2

print(d == d1) #this will false, cause this remebers both the mapping and order of the elements in the dict

#namedtuple
t = (1,2,3,4,5)
print(t[2])

from collections import namedtuple

mobile = namedtuple('mobile', 'brand model price')
m = mobile('samsung','galaxy',1000)
print(m.price) #using name
print(m[2]) #using index


#map function
#The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list. 
# For example:

def even_num(num):
    return num**2
my_list = [1,2,3,4,5,6]
print(list(map(even_num, my_list)))

def str_upper(strr):
    return strr.upper()
my_list = ['sri','blue','mars']
print(list(map(str_upper, my_list)))
for i in map(str_upper, my_list):
    print(i)

def str_upper2(strr):
        if len(strr) % 2 == 0:
                return strr.upper()
        else:
                return strr.lower()
my_list = ['sri','blue','mars','red']
print(list(map(str_upper2, my_list)))

#filter function
#The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.
def str_upper1(strr):
        return len(strr) % 2 == 0

my_list = ['sri','blue','mars','red']
print(list(filter(str_upper1, my_list)))











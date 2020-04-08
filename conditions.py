a = 100
if a%2==0:
    print("even number")
else:
    print("odd number")

#single line
print("even number") if a%2==0 else print("odd number")

for a in range(2,10,2):
    print(a)


i=1
while i<=10:
    print(i)
    i=i+1


for a in range(10):
    if a==5:
        continue
    print(a)


############### NUMBERS ################# 

x=5
print(type(x))
x1=float(x)
print(type(x1))

big=max(10,20,30,40,50)
print(big)
small=min(10,20,30,40,50)
print(small)

a=5
b=10
print(a,b)
a,b=b,a
print(a,b)






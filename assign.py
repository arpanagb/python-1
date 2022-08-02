#python assignment
a=10
b=2
c=a
print("a is c", a is c)
print("a is not b", a is not b)
print("id of a", id(a))
print(id(b))
print(id(c))
#in and not in
x=40
y=25
list=[10,20,30,40,50]
if(x not in list):
    print("x is not in the list")
else:
    print("x is present in given list")
if(y in list):
    print("y is present in given list")
else:
    print(" y is not present in given list")
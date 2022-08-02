l1=["eat","sleep", "repeat"]
s1="python"
obj1=enumerate(l1)
obj2=enumerate(s1)
print("Return type",type(obj1))
print(list(enumerate(l1)))
print(list(enumerate(s1,2)))
print(dict(obj1))
print(list(enumerate(l1,2)))
#python program on while
# m=0
# i=5

# while i>m :
#     print(i, end=" ")
#     i=i-1
# print('end')

for i in range(10):
    print(i)
    if i==2:
        print("break applied")
        break
print("out of loop")
for var in "python world":
    if var=='o':
        continue
    print(var, end=' ')
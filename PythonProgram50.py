# Python Program to Calculate the Average of Numbers in a Given List

#l1=[1,2,3,4,5,6,7]
#ave=Average(l1)
#print(ave)

def Average(lst):
	return sum(lst) / len(lst)

lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

print("Average of the list =", round(average, 2))

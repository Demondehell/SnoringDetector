import numpy as np

x = list(range(1,10,2)) 

print(x)
i=1
x.pop(i)
print(x)
print(x[0:])
print(x[:3])
print(len(x))
x.append(11)
print(len(x))

y =[9,7,8,12,1,3]
print(y)
y.sort()
print(y)


thislist = ["apple", "banana", 12, "apple", 3.9]
print(thislist)



arr = np.array(['1', 2, 3, 4, 5])
print(arr)
arr2 = np.array([1, 2, 3, 4, 5.6])
print(arr2)
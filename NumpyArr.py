import numpy as np

arr = np.array([1, 2, 3, 4, 5])
#print(arr)
#print(type(arr))

arr2 = np.array((1, 2, 3, 4, 5))
#print(arr2)


arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)
#print(arr3[0][1])

print(arr3.transpose())



#arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#print(arr4)
#print(arr4[0][1][2])


#multiplication
#A = np.array([[3, 6, 7], [5, -3, 0]])
#B = np.array([[1, 1], [2, 1], [3, -3]])
#C = A.dot(B)
#print(C)
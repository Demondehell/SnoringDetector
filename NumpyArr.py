import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array((1, 2, 3, 4, 5.2))


print(arr)
print(arr2)
print(arr.shape)
print(arr2.shape)


arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)
print(arr3.shape)
print(arr3[0][1])

print(arr3.transpose())

"""

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr4)
print(arr4[1][1][2])
print(arr4.shape)


arr5 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
print(arr5)
print(arr5[1][1])



#multiplication
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)


D = np.array([[3, 6, 7], [5, -3, 0]])
E = np.array([[3, 6, 7], [5, -3, 0]])
F = D+E
print(F)
"""
import numpy as np

n1 = np.array([10, 20, 30, 40, 50])
n2 = np.array([[20, 30, 40, 50, 60], [24, 55, 13, 15, 18]])
n3 = np.array([1.1, 2.0, 3.2])

print(n1+10)
print(type(n1))
print(n1.dtype)
print(n1.shape)

print(n2+1)
print(type(n2))
print(n2.dtype)
print(n2.shape)

print(n3)
print(type(n3))
print(n3.dtype)
print(n3.shape)

n4 = np.array([[['a', 'b', 'c', 'd'], [1, 2, 3, 4]], [[0, 1, 2, 3], [10, 30, 40, 50]], [[1, 2, 3, 4], [4, 3, 2, 1]]])
print(n4.shape)
print(n4)

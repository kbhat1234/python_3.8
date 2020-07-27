import numpy as np

n1 = np.array([10, 20, 30])
print(n1)
print(n1.ndim)

n2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(n2)
print(n2.ndim)

n3 = np.array([[[1, 2, 3, 4], [4, 3, 2, 1], [20, 20, 30, 40]]])
print(n3)
print(n3.ndim)

n4 = np.zeros((10, 10))
print(n4)
print(n4.ndim)

n5 = np.random.rand(3, 4)
print(n5)

n6 = np.zeros((2, 3))
print(n6)

n7 = np.ones((3, 3))
print(n7)



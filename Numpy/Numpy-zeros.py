import numpy as np

n1 = np.zeros((2, 2), dtype=np.int16, order='F')
print(n1)
print(n1.shape)
print(type(n1))
print(n1.dtype)

n2 = np.ones((1, 2, 3), dtype=np.int16)
print(n2)
print(n2.shape)
print(n2.dtype)
print(type(n2))

import numpy as np

n1 = np.ones((5, 5), dtype=np.int16, order='C')
print(n1)
print(type(n1))
print(n1.dtype)
print(n1.shape)
print(f'Before Re-Shape is \n{n1}')
print(n1.reshape(5, 2))
print(f'After Re-Shape is \n{n1}')

n1.flatten(order='C')
print(f'flatten is {n1}')

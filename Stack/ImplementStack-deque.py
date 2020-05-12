import collections
from collections import deque

stack = deque()
print(stack)
print(type(stack))
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')

print(stack)
print(len(stack))
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# stack.pop()
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Stack/ImplementStack-deque.py", line 20, in <module>
    stack.pop()
IndexError: pop from an empty deque
'''

print(stack)
'''
Output:
deque([])
<class 'collections.deque'>
deque(['A', 'B', 'C', 'D', 'E'])
5
deque(['A', 'B', 'C'])
'''
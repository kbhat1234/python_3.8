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
print(stack)
# stack.pop()
# print(stack)
'''
Output:
deque([])
<class 'collections.deque'>
deque(['A', 'B', 'C', 'D', 'E'])
5
deque(['A', 'B', 'C'])
'''
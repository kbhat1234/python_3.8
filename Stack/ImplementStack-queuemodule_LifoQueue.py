# implement stack using queue
from queue import LifoQueue
from queue import SimpleQueue

stack = LifoQueue(maxsize=3)  # LifoQueue maxsize is 3
print(f'max size is {stack.maxsize}')
'''
max size is 3
'''

print(f'qsize is {stack.qsize()}')
'''
Output:
qsize is 0
'''

print(f'"type(stack)" is {type(stack)}')
'''
Output:
"type(stack)" is <class 'queue.LifoQueue'>
'''

# add elements to stack using put() method
stack.put('A')
stack.put('B')
stack.put('C')
print(f'qsize is {stack.qsize()}')
'''
Output:
qsize is 3
'''

print(stack.full())
'''
Output:
True
'''

print(stack.empty())
'''
Output:
False
'''

print(stack.queue)
'''
Output:
['A', 'B', 'C']
'''

# pop() the element using get() method
stack.get()
stack.get()
stack.get()
stack.get()
print(f'qsize is {stack.qsize()}')
'''
Output:
qsize is 0
'''

print(stack.full())
'''
Output:
False
'''

print(stack.empty())
'''
Output:
True
'''

print(stack.queue)
'''
Output:
[]
'''

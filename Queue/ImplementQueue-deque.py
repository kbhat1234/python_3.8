import collections
from collections import deque


# implement queue using collections.deque
def queue_display():
    print(f'queue is {q}')
    print(f'"type(q)" is {type(q)}')


q = deque()
queue_display()
'''
Output:
queue is deque([])
"type(q)" is <class 'collections.deque'>
'''

print('-----adding elements to queue-----')
q.append('A')  # 'A' is added to the queue d
q.append('B')
q.append('C')
q.append('D')
queue_display()
'''
Output:
-----adding elements to queue-----
queue is deque(['A', 'B', 'C', 'D'])
"type(q)" is <class 'collections.deque'>
'''

print('----removing elements from queue----')
q.popleft()  # 'A' is removed from the queue d
q.popleft()
queue_display()
'''
Output:
----removing elements from queue----
queue is deque(['C', 'D'])
"type(q)" is <class 'collections.deque'>
'''

print('----removing all elements from queue----')
q.popleft()
q.popleft()
queue_display()
'''
Output:
----removing all elements from queue----
queue is deque([])
"type(q)" is <class 'collections.deque'>
'''

# print('----removing elements when queue is empty-----')
# q.popleft()
# queue_display()
'''
Output:
IndexError: pop from an empty deque
'''
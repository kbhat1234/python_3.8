from collections import deque


# implement queue using collections.deque
def deque_display():
    print(f'queue is {d}')
    print(f'"type(d)" is {type(d)}')


d = deque()
deque_display()
'''
Output:
deque([])
<class 'collections.deque'>
'''

print('-----adding elements to queue-----')
d.append('A')  # 'A' is added to the queue d
d.append('B')
d.append('C')
d.append('D')
deque_display()
'''
Output:
deque(['A', 'B', 'C', 'D'])
<class 'collections.deque'>
'''

print('----removing elements from queue----')
d.popleft()  # 'A' is removed from the queue d
d.popleft()
d.popleft()
d.popleft()
# d.popleft()
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Queue/ImplementQueue-deque.py", line 35, in <module>
    d.popleft()
IndexError: pop from an empty deque
'''
deque_display()
'''
Output:
deque(['C', 'D'])
<class 'collections.deque'>
'''
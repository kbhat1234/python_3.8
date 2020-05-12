# implement queue using queue.Queue
import queue
from queue import Queue


def queue_display():
    print(f'queue max size is {q.maxsize}')
    print(f'queue elements is {q.queue}')
    print(f'queue size is {q.qsize()}')
    print(f'"type(l)" is {type(q)}')
    print(f'queue is full {q.full()}')
    print(f'queue is empty {q.empty()}')


q = Queue(maxsize=5)
queue_display()
'''
Output:
queue max size is 5
queue elements is deque([])
queue size is 0
"type(q)" is <class 'queue.Queue'>
'''

print('----adding elements to queue (QUEUE ENQUEUE)-----')
q.put('A')  # 'A' added from rear end of queue
q.put('B')  # 'B' added from rear end of queue
q.put('C')
q.put('D')
q.put('E')
queue_display()  # queue_display() function call to display details of queue
'''
Output:
----adding elements to queue (QUEUE ENQUEUE)-----
queue max size is 5
queue elements is deque(['A', 'B', 'C', 'D', 'E'])
queue size is 5
"type(q)" is <class 'queue.Queue'>
'''

print('----removing elements from queue (QUEUE DEQUEUE-----')
q.get()  # 'A' removed from front end of queue
q.get()  # 'B' removed from front end of queue
queue_display()  # queue_display() function call to display details of queue
'''
Output:
----deleting elements from queue (QUEUE DEQUEUE-----
queue max size is 5
queue elements is deque(['C', 'D', 'E'])
queue size is 3
"type(q)" is <class 'queue.Queue'>
'''

print('---removing all elements from queue------')
q.get()
q.get()
q.get()
queue_display()
'''
Output:
---removing all elements from queue------
queue max size is 5
queue elements is deque([])
queue size is 0
"type(q)" is <class 'queue.Queue'>
'''

print('---removing element when queue is empty------')
q.get()
queue_display()
'''
Output:
No error seen on IndexError
'''
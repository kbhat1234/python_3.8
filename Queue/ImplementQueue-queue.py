# implement queue using queue.Queue
import queue
from queue import Queue


def queue_display():
    print(f'queue max size is {l.maxsize}')
    print(f'queue elements is {l.queue}')
    print(f'queue size is {l.qsize()}')
    print(f'"type(l)" is {type(l)}')


l = Queue(maxsize=5)
queue_display()
'''
Output:
queue max size is 5
queue elements is deque([])
queue size is 0
"type(l)" is <class 'queue.Queue'>
'''

print('----adding elements to queue (QUEUE ENQUEUE)-----')
l.put('A')  # 'A' added from rear end of queue
l.put('B')  # 'B' added from rear end of queue
l.put('C')
l.put('D')
l.put('E')
queue_display()  # queue_display() function call to display details of queue
'''
Output:
----adding elements to queue (QUEUE ENQUEUE)-----
queue max size is 5
queue elements is deque(['A', 'B', 'C', 'D', 'E'])
queue size is 5
"type(l)" is <class 'queue.Queue'>
'''

print('----deleting elements from queue (QUEUE DEQUEUE-----')
l.get()  # 'A' removed from front end of queue
l.get()  # 'B' removed from front end of queue
queue_display()  # queue_display() function call to display details of queue
'''
Output:
----deleting elements from queue (QUEUE DEQUEUE-----
queue max size is 5
queue elements is deque(['C', 'D', 'E'])
queue size is 3
"type(l)" is <class 'queue.Queue'>
'''
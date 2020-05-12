from queue import Queue


def Queue_display():
    print(f'queue max size is {q.maxsize}')
    print(q.empty())
    print(q.full())
    print(f'queue size is {q.qsize()}')
    print(f'queue elements is {q.queue}')


q = Queue(maxsize=5)

print('----adding elements to queue----')
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
Queue_display()
'''
Output:
----adding elements to queue----
queue max size is 5
queue size is 5
queue elements is deque(['A', 'B', 'C', 'D', 'E'])
'''

print('----removing elements from queue-----')
q.get()
q.get()
Queue_display()
'''
Output:
----removing elements from queue-----
queue max size is 5
queue size is 3
queue elements is deque(['C', 'D', 'E'])
'''
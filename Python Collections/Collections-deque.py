import collections as c

# list l1
l1 = [10, 20, 40, 5, 2, 6, True, False, None]
print(f'l1 elements is {l1}')
print(f'"type(l1)" is {type(l1)}')
'''
Output:
l1 elements is [10, 20, 40, 5, 2, 6, True, False, None]
"type(l1)" is <class 'list'>
'''

# deque(l1)
l = c.deque(l1)
l.appendleft(20)
l.appendleft(9)
l.append(100)
l.append(200)
l.pop()
l.popleft()
print(f'deque elements is {l}')
print(f'"type(l)" is {type(l)}')
'''
Output:
deque elements is deque([10, 20, 40, 5, 2, 6, True, False, None])
"type(l)" is <class 'collections.deque'>
'''

# tuple t1
t1 = (20, 'karthik', 'a', True, False, None)
print(f't1 elements is {t1}')
print(f'"type(t1)" is {type(t1)}')
'''
Output:
t1 elements is (20, 'karthik', 'a', True, False, None)
"type(t1)" is <class 'tuple'>
'''

# deque(t1)
t = c.deque(t1)
print(f'deque elements is {t}')
print(f'"type(t)" is {type(t)}')
'''
Output:
deque elements is deque([20, 'karthik', 'a', True, False, None])
"type(t)" is <class 'collections.deque'>
'''

# dictionary d1
d1 = {'name': 'karthik', 'age': 40, 'mobile': True, 'phone': False, 'address': None}
print(f'd1 elements is {d1}')
print(f'"type(d1)" is {type(d1)}')
'''
Output:
d1 elements is {'name': 'karthik', 'age': 40, 'mobile': True, 'phone': False, 'address': None}
"type(d1)" is <class 'dict'>
'''

# deque(d1.keys())
k = c.deque(d1.keys())
print(f'deque elements is {k}')
print(f'"type(k)" is {type(k)}')
'''
Output:
deque elements is deque(['name', 'age', 'mobile', 'phone', 'address'])
"type(k)" is <class 'collections.deque'>
'''

# deque(d1.values())
v = c.deque(d1.values())
print(f'deque elements is {v}')
print(f'"type(v)" is {type(v)}')
'''
Output:
deque elements is deque(['karthik', 40, True, False, None])
"type(v)" is <class 'collections.deque'>
'''
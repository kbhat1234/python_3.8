t1 = ()  # empty tuple
print(f'tuple t1 is {t1}')
print(f'tuple t1 is {t1[:]}')
print(f'type(t1) is {type(t1)}')
'''
Output:
tuple t1 is ()
tuple t1 is ()
type(t1) is <class 'tuple'>
'''
# print(t1[0])
'''
Output:
"C:\Program Files\Python38\python.exe" "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Tuples/TupleSimpleOperation.py"
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Tuples/TupleSimpleOperation.py", line 3, in <module>
    print(t1[0])
IndexError: tuple index out of range
tuple t1 is ()
'''

t2 = (1,)  # tuple with one element
print(f'tuple t2 is {t2}')
print(f't2[{0}] is {t2[0]}')
print(f'type(t2) is {type(t2)}')
print(f'type(t2[{0}]) is {type(t2[0])}')
'''
Output:
tuple t2 is (1,)
t2[0] is 1
type(t2) is <class 'tuple'>
type(t2[0]) is <class 'int'>
'''

t3 = (1, 2, 3, 4, 5)  # tuple with only integer values
print(f'tuple t3 is {t3}')
print(f't3[{3}] is {t3[3]}')
print(f't3[{0}:{2}] is {t3[0:2]}')
print(f't3[{0}:] is {t3[0:]}')
print(f't3[:{3}] is {t3[:3]}')
print(f't3[{3}:{4}] is {t3[3:4]}')
print(f't3[{-1}] is {t3[-1]}')
print(f't3[{-4}:{-1}] is {t3[-4:-1]}')
print(f'type(t3) is {type(t3)}')
print(f'type(t3[{4}]) is {type(t3[4])}')
'''
Output:
tuple t3 is (1, 2, 3, 4, 5)
t3[3] is 4
t3[0:2] is (1, 2)
t3[0:] is (1, 2, 3, 4, 5)
t3[:3] is (1, 2, 3)
t3[3:4] is (4,)
t3[-1] is 5
t3[-4:-1] is (2, 3, 4)
type(t3) is <class 'tuple'>
type(t3[4]) is <class 'int'>
'''

t4 = ('apple', 'orange', 'banana')  # tuple with only string values
print(f'tuple t4 is {t4}')
print(f't4[{1}] is {t4[1]}')
print(f'type(t4) is {type(t4)}')
print(f'type(t4[{1}] is {type(t4[1])}')
'''
Output:
tuple t4 is ('apple', 'orange', 'banana')
t4[1] is orange
type(t4) is <class 'tuple'>
type(t4[1] is <class 'str'>
'''

t5 = ('apple', 24, 'a', 2)  # tuple with both numbers and string values
print(f'tuple t5 is {t5}')
print(f't5[{2}] is {t5[2]}')
print(f'type(t5) is {type(t5)}')
print(f'type(t5[{2}] is {type(t5[2])}')
print(f'type(t5[{1}] is {type(t5[1])}')
'''
Output:
tuple t5 is ('apple', 24, 'a', 2)
t5[2] is a
type(t5) is <class 'tuple'>
type(t5[2] is <class 'str'>
type(t5[1] is <class 'int'>
'''

# printing the tuple elements with the index
#tuple1 = (10, 20, 30, 40, 50, 60)
tuple1 = (2, 'a', 3, 'b')
print(tuple1)
'''
Output:
(10, 20, 30, 40, 50, 60)
'''
count = 0
for i in tuple1:
    print(f'tuple1[{count}] = {i}')
    count += 1
'''
Output:
tuple1[0] = 10
tuple1[1] = 20
tuple1[2] = 30
tuple1[3] = 40
tuple1[4] = 50
tuple1[5] = 60
'''

# input elements using the input to a tuple
tuple1 = tuple(input('enter the tuple elements here '))
count = 0
for i in tuple1:
    print(f'tuple1[{count}] = {i}')
    count += 1
'''
Output:
enter the tuple elements here 12345
tuple1[0] = 1
tuple1[1] = 2
tuple1[2] = 3
tuple1[3] = 4
tuple1[4] = 5
'''

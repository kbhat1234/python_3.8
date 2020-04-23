# pop() method to remove elements arbitarly from the set
set1 = {1, 2, 3, 4, 5}
print(f'set1 is {set1}')
'''
Output:
set1 is {1, 2, 3, 4, 5}
'''
e1 = set1.pop()  # it removes an element arbitarily from set
print(f'{e1} is removed from set1')
print(f'set1 updated is {set1}')
'''
Output:
1 is removed from set1
set1 updated is {2, 3, 4, 5}
'''
set1.clear()  # removing all elements from set, set is empty
# e2 = set1.pop()  # trying to execute pop() operation will lead to KeyError exception
print(f'set1 is {set1}')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-pop.py", line 17, in <module>
    e2 = set1.pop()  # trying to execute pop() operation will lead to KeyError exception
KeyError: 'pop from an empty set'
'''

del set1  # using del keyword we can delete the set1
# print(set1)  # NameError is seen as the object set1 is not defined
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-pop.py", line 28, in <module>
    print(set1)  # NameError is seen as the object set1 is not defined
NameError: name 'set1' is not defined
'''

# diff between discard() and remove()
days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
print(f'days is {days}')
'''
Output:
days is {'sunday', 'monday', 'wednesday', 'saturday', 'tuesday', 'thursday', 'friday'}
'''
# remove element from set using discard() method when element not present in the set days
days.discard('Tuesday')  # Tuesday is not in set days, no error seen python maintains the control flow
print(f'days is {days}')
days.clear()
days.discard('TUESDAY')  # Tuesday is not in set days.
print(f'days is {days}')

# remove element from set using remove() method when element is not present in the set days
# days.remove('Tuesday')  # Tuesday is not in set days, KeyError seen
print(f'days is {days}')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-pop.py", line 52, in <module>
    days.remove('Tuesday')  # Tuesday is not in set days, KeyError seen
KeyError: 'Tuesday'
'''
days.clear()
days.remove('TUESDAY')  # TUESDAY is not in set days.
print(f'days is {days}')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-pop.py", line 62, in <module>
    days.remove('TUESDAY')  # Tuesday is not in set days.
KeyError: 'TUESDAY'
'''

set1 = {'a', 12.34, 87.56, 'karthik', 'apple'}
print(f'set1 is {set1}')
'''
Output:
set1 is {'karthik', 'apple', 12.34, 'a', 87.56}
'''
# print(set1.remove(87.56))
set1.remove(12.34)  # element 12.34 is present in set
print(f'set1 is {set1}')
'''
Output:
set1 is {'karthik', 'apple', 'a', 87.56}
'''
set1.remove(200)  # element 'Karthik' is not in set, will throw key error
print(f'set1 is {set1}')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-remove.py", line 15, in <module>
    set1.remove(200)  # element 'Karthik' is not in set, will throw key error
KeyError: 200
'''
# create a dictionary with keys immutable (duplicate keys)
dic1 = {1: 'apple', 1: 'orange', 1: 'pineapple', 1: 'watermelon', 1: 'litchi'}
print(type(dic1[1]))
print(f'dic1 items is {dic1.items()}')
'''
Output:
dic1 items is dict_items([(1, 'litchi')])
<class 'str'>
'''
print(f'dic1 is {dic1}')
'''
Output:
{1: 'litchi'}
'''
print(f'dic1 keys is {dic1.keys()}')
'''
Output:
dict_keys is dict_keys([1])
'''
print(f'dic1 values is {dic1.values()}')
'''
Output:
dic1 values is dict_values(['litchi'])
'''
print(f'type(dic1) is {type(dic1)}')
print('------------------------------------------------------------------------------------------------')

# duplicate keys in different order defined
dic2 = {1: 'karthik', 2: 'rini', 3: 'ishani', 2: 'kaustubh'}
print(f'dic2 is {dic2}')
'''
Output:
dic2 is {{1: 'karthik', 2: 'kaustubh', 3: 'ishani'}
'''
print(f'dic2 items is {dic2.items()}')
'''
Output:
dic2 items is dict_items([(1, 'karthik'), (2, 'kaustubh'), (3, 'ishani')])
'''
print(f'dic2 keys is {dic2.keys()}')
'''
Output:
dic2 keys is dict_keys([1, 2, 3])
'''
print(f'dic2 values is {dic2.values()}')
'''
Output:
dic2 values is dict_values(['karthik', 'kasutubh', 'ishani'])
'''
print('------------------------------------------------------------------------------------------------------')

# dictionary key is tuple of values
dic3 = {(1, 2, 3): 'karthik', (4, 5, 6): 'karthik', (7, 8, 9): 'ishani', (10, 11, 12): 'kaustubh',
        (13, 14, 15): 'ishani'}
print(f'dic3 items is {dic3.items()}')
'''
Output:
dic3 items is dict_items([((1, 2, 3), 'karthik'), ((4, 5, 6), 'karthik'), ((7, 8, 9), 'ishani'), ((10, 11, 12), 'kaustubh'), ((13, 14, 15), 'ishani')])
'''
print(f'dic3 is {dic3}')
'''
Output:
dic3 is {(1, 2, 3): 'karthik', (4, 5, 6): 'karthik', (7, 8, 9): 'ishani', (10, 11, 12): 'kaustubh', (13, 14, 15): 'ishani'}
'''
print(f'dic3 keys is {dic3.keys()}')
'''
Output:
dic3 keys is dict_keys([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)])
'''
print(f'dic3 values is {dic3.values()}')
'''
Output:
dic3 values is dict_values(['karthik', 'karthik', 'ishani', 'kaustubh', 'ishani'])
'''
print(f'dic3[({1}, {2}, {3})]) is {dic3[(1, 2, 3)]}')
'''
Output:
dic3[(1, 2, 3)] is karthik
'''
print('----------------------------------------------------------------------------------------')

dic4 = {1: 'karthik', 'name': 'bhat', 1: 55454, 1: (2, 3, 4)}
print(dic4)
print(type(dic4[1]))
'''
Output:
{1: (2, 3, 4), 'name': 'bhat'}
<class 'str'>
'''
print(type(dic4))
'''
Output:
<class 'dict'>
'''
st = str(dic4)
print(st)
print(type(st))
'''
Output:
{1: (2, 3, 4), 'name': 'bhat'}
<class 'str'>
'''

dic5 = {'fname': 'karthik', 'lname': 'bhat', 'age': 41, 'empid': 'ajppb4129b'}
print("fname is %s" % dic5['fname'])
print(type(dic5['age']))
'''
Output:
fname is karthik
<class 'int'>
'''
print("fname is %s" % dic5['fname'], ", lname is %s" % dic5['lname'], ", age is %d" % dic5['age'],
      ", empid is %s" % dic5['empid'])
'''
Output:
name is karthik , lname is bhat , age is 41 , empid is ajppb4129b
'''
print(dic5)
print('karthik' not in dic5['fname'])
print('Karthik' in dic5['fname'])
'''
Output:
{'fname': 'karthik', 'lname': 'bhat', 'age': 41, 'empid': 'ajppb4129b'}
False
False
'''

# accessing dictionary values using indexing with keys and get() method
d = {1: 'apple', 2: 'orange', 3: 'pineapple', 4: 'guava', 5: 'litchi'}
print(f'd is {d}')
print(f'type(d) is {type(d)}')
'''
Output:
d is {1: 'apple', 2: 'orange', 3: 'pineapple', 4: 'guava', 5: 'litchi'}
type(d) is <class 'dict'>
'''
dk = d.keys()
dv = d.values()
print(f'd keys is {dk}')
'''
Output:
d keys is dict_keys([1, 2, 3, 4, 5])
'''
print(f'd values is {dv}')
'''
Output:
d values is dict_values(['apple', 'orange', 'pineapple', 'guava', 'litchi'])
'''
di = d.items()
print(f'd items is {di}')
'''
Output:
d items is dict_items([(1, 'apple'), (2, 'orange'), (3, 'pineapple'), (4, 'guava'), (5, 'litchi')])
'''
print("1: %s" % d[1], "\n2: %s" % d[2], "\n3: %s" % d[3], "\n4: %s" % d[4], "\n5: %s" % d[5])
'''
Output:
1: apple 
2: orange 
3: pineapple 
4: guava 
5: litchi
'''
print(f'1: {d.get(1)} \n2: {d.get(2)} \n3: {d.get(3)} \n4: {d.get(4)} \n5: {d.get(5)}')
'''
Output:
1: apple 
2: orange 
3: pineapple 
4: guava 
5: litchi
'''

d1 = {'name': 'karthik', 'age': 41, 'salary': 250000, 'company': 'onmobile'}
print(f"name: {d1.get('name')}, age: {d1.get('age')}, salary: {d1.get('salary')}, company: {d1.get('company')}")
'''
Output:
name: karthik, age: 41, salary: 250000, company: onmobile
'''

# 1. properties of dictionary - same key defined multiple times for holding multiple values
employee = {'name': 'karthik', 'age': 41, 'salary': 25000.00, 'company': 'GOOGLE', 'name': 'ishani'}
print(f'employee dictionary is {employee}')

# using items() method
for x, y in employee.items():
    print(x, y)
print('end of program')

# using items() method
for i in employee.items():
    print(i)
print('end of program')

# 2. properties of dictionary - key cannot be list
dic1 = {'name': 'karthik', 'empid': 232323, [100, 200, 300]: 'cse'}
print(dic1)

for x, y in dic1.items():
    print(x, y)
print('end of program')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Dictionary/PythonDictionary.py", line 196, in <module>
    dic1 = {'name': 'karthik', 'empid': 232323, [100, 200, 300]: 'cse'}
TypeError: unhashable type: 'list'
'''
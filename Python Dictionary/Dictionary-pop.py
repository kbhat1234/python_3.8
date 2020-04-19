dic = {1: 'apple', 2: 'orange', 3: 'grapes', 4: 'mango', 5: 'banana'}
print(f'dic is {dic}')
'''
Output:
dic is {1: 'apple', 2: 'orange', 3: 'grapes', 4: 'mango', 5: 'banana'}
'''

# valid key present in dictionary
result = dic.pop(5)
print(f'popped element is {result}')
print(f'dic after popped out element is {dic}')
'''
Output:
popped element is banana
dic after popped out element is {1: 'apple', 2: 'orange', 3: 'grapes', 4: 'mango'}
'''

# invalid key/key not present in dictionary, but default message is provided
res = dic.pop(6, 'no element found in dic')
print(f'popped out element is {res}')
print(f'dic after pop is {dic}')
'''
Output:
popped out element is no element found in dic
dic after pop is {1: 'apple', 2: 'orange', 3: 'grapes', 4: 'mango'}
'''

# key not present in dictionary and no default message provided
#res1 = dic.pop(7)  # KeyError shown
#print(res1)
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Dictionary/Dictionary-pop.py", line 12, in <module>
    res1 = dic.pop(7)
KeyError: 7
'''
# python stack implementation using list

list1 = []  # empty list
print(list1)
list1.append('A')  # 'A' is pushed to list1 (as stack)
list1.append('B')  # 'B' is pushed to list1
list1.append('C')  # 'C' is pushed to list1
list1.append('D')  # 'D' is pushed to list1
list1.append('E')  # 'E' is pushed to list1
list1.append('E')  # duplicate item is allowed
list1.append('B')  # duplicate item is allowed

print(list1)  # print the list1
print(f'original stack elements is {list1}')  # print the stack elements

p = list1.pop()  # pop() topmost element from list (as stack)
print(f'{p} is removed from list1')  # 'E' item is removed from list (as stack)
print(f'stack elements after pop operation is {list1}')  # print list1 elements (as stack) after pop() operation
print(len(list1))
list1.pop()
list1.pop()
list1.pop()
list1.pop()
list1.pop()
list1.pop()
print(len(list1))
# list1.pop()  # at this point IndexError is seen
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Stack/ImplementStack-list.py", line 24, in <module>
    list1.pop()
IndexError: pop from empty list
'''
print(list1)
print(len(list1))
'''
Output:
['A', 'B', 'C', 'D', 'E', 'E', 'B']
original stack elements is ['A', 'B', 'C', 'D', 'E', 'E', 'B']
B is removed from list1
stack elements after pop operation is ['A', 'B', 'C', 'D', 'E', 'E']
[]
'''
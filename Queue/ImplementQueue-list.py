# implement queue using list
def list_display():
    print(f'"len(l)" is {len(l)}')
    print(f'"type(l)" is {type(l)}')
    print(f'list elements is {l}')

l = []  # empty list
list_display()
'''
Output:
"len(l)" is 0
"type(l)" is <class 'list'>
list elements is []
'''

print('-----adding elements to queue using list-----')
l.append('A')
l.append('B')
l.append('C')
l.append('D')
list_display()
'''
Output:
-----adding elements to queue using list-----
"len(l)" is 4
"type(l)" is <class 'list'>
list elements is ['A', 'B', 'C', 'D']
'''

print('-----removing elements from queue using list-----')
l.pop(0)  # 'A' is removed
l.pop(0)  # 'B' is removed
list_display()
'''
Output:
-----removing elements from queue using list-----
"len(l)" is 2
"type(l)" is <class 'list'>
list elements is ['C', 'D']
'''

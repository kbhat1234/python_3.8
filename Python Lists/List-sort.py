'''
list sort() method used to sort the list, default it sort by ascending order
'''
l1 = ['chetan', 'ashish', 'karthik', 'ishani', 'kaustubh']  # string list
l2 = [20, 4, 2, 19, 24, 15]  # int list

print(f'list l1 before sorting is {l1}')
print(f'list l2 before sorting is {l2}')
'''
Output:
list l1 before sorting is ['chetan', 'ashish', 'karthik', 'ishani', 'kaustubh']
list l2 before sorting is [20, 4, 2, 19, 24, 15]
'''

l1.sort(reverse=False)  # default sort by ascending order with no such argument reverse=False (sort by Ascending order), reverse=True (sort by Decending order)
l2.sort(reverse=False)  # default sort by ascending order with no such argument

print(f'list l1 after sorting {l1}')
print(f'list l2 after sorting {l2}')
'''
Output:
list l1 after sorting ['ashish', 'chetan', 'ishani', 'karthik', 'kaustubh']
list l2 after sorting [2, 4, 15, 19, 20, 24]
'''
l3 = ['chetan', 'ashish', 'karthik', 'ishani', 'kaustubh']
l4 = [20, 4, 2, 19, 24, 15]

l3.sort(reverse=True)  # sort by descending order
l4.sort(reverse=True)  # sort by descending order

print(f'list l3 after sorting {l3}')
print(f'list l4 after sorting {l4}')
'''
Output:
list l3 after sorting ['kaustubh', 'karthik', 'ishani', 'chetan', 'ashish']
list l4 after sorting [24, 20, 19, 15, 4, 2]
'''

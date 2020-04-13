# count(x) will count the number of occurences of given element

list = ['karthik', 'ishani', 'kaustubh', 'anika', 'manushi', 'karthik', 'aditya', 'aditya']
count = list.count('karthik')
print(f'count({"karthik"}) is {count}')
'''
Output:
count({"karthik"}) is 2
'''

# count the occurences of given element when it is not in list
count1 = list.count('rini')
print(f'count({"rini"}) is {count1}')
'''
Output:
count({"Karthik"}) is 0
'''

# check the elements are duplicate in list
count2 = list.count('karthik')  # check for having duplicates
if count2 >= 2:
    print(f'element in list is having duplicates')
else:
    print(f'element in list is not having duplicates')

print(f'count({"karthik"}) is {count2}')
'''
Output:
element in list is not having duplicates
count(karthik) is 0
'''

count3 = list.count('kaustubh')  # no duplicates
if count3 == 1:
    print(f'element in list do not have duplicates')
else:
    print(f'element in list having duplicates')

print(f'count({"kaustubh"}) is {count3}')
'''
Output:
element in list do not have duplicates
count(kaustubh) is 1
'''
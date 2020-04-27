# call by reference - using mutable object list, dictionary, set
# defining the function


def change_list(list1):
    list1.append(20)
    list1.append(50)
    print(f'list inside function is {list1}')


def change_dic(dic1):
    dic1.update({40: 'rini', 50: 'ashish'})
    print(f'dic inside function is {dic1}')
    print(f'keys of dic is {dic1.keys()}')
    print(f'values of dic is {dic1.values()}')


list = [10, 30, 40, 60]
change_list(list)
'''
Output:
list inside function is [10, 30, 40, 60, 20, 50]
'''
print(f'list outside function is {list}')
'''
Output:
list outside function is [10, 30, 40, 60, 20, 50]
'''

dic = {10: 'karthik', 20: 'ishani', 30: 'kaustubh'}
change_dic(dic)
'''
Output:
dic inside function is {10: 'karthik', 20: 'ishani', 30: 'kaustubh', 40: 'rini', 50: 'ashish'}
keys of dic is dict_keys([10, 20, 30, 40, 50])
values of dic is dict_values(['karthik', 'ishani', 'kaustubh', 'rini', 'ashish'])
'''
print(f'dic outside function is {dic}')
print(f'keys of dic is {dic.keys()}')
print(f'values of dic is {dic.values()}')
'''
Output:
dic outside function is {10: 'karthik', 20: 'ishani', 30: 'kaustubh', 40: 'rini', 50: 'ashish'}
keys of dic is dict_keys([10, 20, 30, 40, 50])
values of dic is dict_values(['karthik', 'ishani', 'kaustubh', 'rini', 'ashish'])
'''


# call by reference - using immutable objects tuple, string
# defing function


def change_string(str1):
    str1 = str1 + 'How r u'
    print(f'printing string inside the function {str1}')


string1 = 'karthik, '
change_string(string1)  # calling the function
'''
Output:
printing string inside the function karthik, How r u
'''
print(f'printing string outside the function {string1}')
'''
Output:
printing string outside the function karthik, 
'''
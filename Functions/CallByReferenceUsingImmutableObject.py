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
# isdigit() string method
digit1 = '12334'
print(digit1.isdigit())
'''
Output:
True
'''

digit2 = '12343 '
print(digit2.isdigit())
'''
Output:
False
'''

digit3 = '1234@@23##'
print(digit3.isdigit())
'''
Output:
False
'''

digit4 = '123-444-223-346'
if digit4.isdigit() is True:
    print('string contains only digits')
else:
    print('string not contain digits')

'''
Output:
string not contain digits
'''
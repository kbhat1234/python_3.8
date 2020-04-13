# isdecimal() string method
str1 = 'welcome'
print(str1.isdecimal())
'''
Output:
False
'''

str2 = '123'
print(str2.isdecimal())
'''
Output:
True
'''

str3 = '123 '
print(str3.isdecimal())
'''
Output:
False
'''

str4 ='123#$'
print(str4.isdecimal())
'''
Output:
False
'''

if str2.isdecimal() is True:
    print('string is a valid decimal number')
else:
    print('string is not a valid decimal number')
'''
Output:
string is a valid decimal number
'''
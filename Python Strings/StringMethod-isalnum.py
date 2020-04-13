# isalnum() string method
print('isalnum() method')
alnum1 = 'karthik'
print(alnum1.isalnum())
'''
Output:
True
'''

alnum2 = 'Welcome '
print(alnum2.isalnum())
'''
Output:
False
'''

alnum3 = 'Welcome123'
print(alnum3.isalnum())
'''
Output:
True
'''

alnum4 = 'Welcome 123'
print(alnum4.isalnum())
'''
Output:
False
'''

alnum5 = '12324234'
print(alnum5.isalnum())
'''
Output:
True
'''

alnum6 = '12324234 '
print(alnum6.isalnum())
'''
Output:
False
'''

alnum7 = '123@$$'
print(alnum7.isalnum())
'''
Output:
False
'''

if alnum1.isalnum() is True:
    print('string is a valid alphanumeric')
else:
    print('string is not a valid alphanumeric')
'''
Output:
string is a valid alphanumeric
'''
# isupper() string method
s1 = 'HELLO WORLD !!! WELCOME TO PYTHON PROGRAMMING'
print(s1.isupper())
'''
Output:
True
'''

s2 = 'Hello World 2376 welcome to pyhton programming'
print(s2.isupper())
'''
Output:
False
'''

if s1.isupper() is True:
    print('string is in upper case')
else:
    print('string is not in upper case')
'''
Output:
string is in upper case
'''
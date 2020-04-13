# islower() string method
s1 = 'welcome to jungle gnr'
print(s1.islower())
'''
Output:
True
'''

s2 = 'Welcome to Jungle GNR'
print(s2.islower())
'''
Output:
False
'''

if s1.islower() is True:
    print('string is lower')
else:
    print('string is not lower')
'''
String is lower
'''
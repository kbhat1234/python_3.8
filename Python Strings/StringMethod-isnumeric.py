# isnumeric() string method
s1 = '23633446345'
print(s1.isnumeric())
'''
Output:
True
'''

s2 = '2332 '
print(s2.isnumeric())
'''
Output:
False
'''

s3 = '23763java@##'
print(s3.isnumeric())
'''
Output:
False
'''

if s1.isnumeric() is True:
    print('string is a valid numeric')
else:
    print('string is not a valid numeric')
'''
Output:
string is a valid numeric
'''
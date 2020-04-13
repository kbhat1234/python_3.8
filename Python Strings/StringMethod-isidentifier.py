# isidentifier() string method

s1 = 'welcome'
print(s1.isidentifier())
'''
Output:
True
'''

s2 = 'welocme420'
print(s2.isidentifier())
'''
Output:
True
'''

s3 = 'welcome_420'
print(s3.isidentifier())
'''
Output:
True
'''

s4 = '@karthik420'
print(s4.isidentifier())
'''
Output:
False
'''

s5 ='karthik 343#'
print(s5.isidentifier())
'''
Output:
False
'''

if s1.isidentifier() is True:
    print('string is valid identifier')
else:
    print('string is not valid identifier')

'''
Output:
string is valid identifier
'''
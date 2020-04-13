# title() string method
stitle = 'bANgalOre'
print(stitle.title())
'''
given string as stitle = 'bANgalOre'
Output:
Bangalore
'''

t = stitle.title()
print(t.istitle())
'''
Output:
True
'''

if t.istitle() is True:
    print('string is title')
else:
    print('string is not title')
'''
Output:
string is title
'''


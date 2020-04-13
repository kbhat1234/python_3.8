# isalpha() string method
alpha1 = 'welcome'
print(alpha1.isalpha())
'''
Output:
True
'''

alpha2 = 'welcome '
print(alpha2.isalpha())
'''
Output:
False
'''

alpha3 = 'welcomejava'
if alpha3.isalpha() is True:
    print("String contains alphabets")
else:
    print("String contains other characters")
'''
Output:
String contains alphabets
'''

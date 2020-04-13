# isprintable() string method
ps1 = 'Hello world!!!'
print(ps1.isprintable())
'''
Output:
True
'''

ps2 = 'Hello@world $$$$'
print(ps2.isprintable())
'''
Output:
True
'''

ps3 = 'Hello\nWorld\tWelcome to python'
print(ps3.isprintable())
'''
Output:
False
'''

if ps1.isprintable() is True:
    print('string is printable')
else:
    print('string is not printable')

'''
Output:
string is printable
'''
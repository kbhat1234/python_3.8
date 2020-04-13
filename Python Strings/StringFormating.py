msg1 = 'Python beginners guide'
msg2 = "Welcome to python's guide"
msg3 = 'Welcome to "jungle"'
msg4 = '''\n
Hi John,

first email.

Thanks
Karthik\n
'''
format_str = f'{msg1} [{msg2}] is a coder'
print(format_str)

msg1_char = len(msg1)
print(f'Length of the string msg1 is {msg1_char}')

msg2_char = len(msg2)
print(f'Length of the string msg2 is {msg2_char}')

print(f'msg1 is {msg1}')
print(f'msg2 is {msg2}')
print(f'msg3 is {msg3}')
print(f'msg4 is {msg4}')

''' msg1 -> P '''
print(f'msg1 is {msg1[0]}')

''' msg1 -> Pyth '''
print(f'msg1 is {msg1[0:4]}')

''' msg1 -> Pyth '''
print(f'msg1 is {msg1[:4]}')

''' msg1 -> thon beginners guide '''
print(f'msg1 is {msg1[2:]}')

''' msg1 -> Python beginners guide '''
print(f'msg1 is {msg1[:]}')

''' msg2 -> e '''
print(f'msg2 is {msg2[-1]}')

''' msg2 -> Welcome to python's guid '''
print(f'msg2 is {msg2[0:-1]}')

''' msg2 -> lcome to python's gui '''
print(f'msg2 is {msg2[2:-2]}')

''' msg2 -> uid '''
print(f'msg2 is {msg2[-4:-1]}')
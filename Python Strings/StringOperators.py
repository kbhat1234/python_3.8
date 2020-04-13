s1 = 'Hello welcome to python world of programming '
s2 = '"Python is easy, robust and simple to learn'

print(f'concatenation of strings s1 and s2 is -> {s1 + s2}')
'''
Output:
concatenation of strings s1 and s2 is -> Hello welcome to python world of programming "Python is easy, robust and simple to learn
'''

print(f'repetitions of string s1 is -> {s1 * 2}')
'''
Output:
repetitions of string s1 is -> Hello welcome to python world of programming Hello welcome to python world of programming
'''

print(f'{s1[6]}')
'''
Output:
w
'''

print(f'{s1[2:8]}')
'''
Output:
llo we
'''

print(f"{'python' in s1}")
'''
Output:
True
'''

print(f"{'Python' not in s1}")
'''
Output:
True
'''

print(r'C:\\Apps\\SupportAssist\\x64\\plugin_installer\\DellUpdateSupportAssistPlugin.msi')
'''
Output:
C:\\Apps\\SupportAssist\\x64\\plugin_installer\\DellUpdateSupportAssistPlugin.msi
'''

print("The string s1 : %s" % s1)
'''
Output:
The string s1 : Hello welcome to python world of programming
'''

Integer = 10
Float = 23.88
String = 'Welcome to Jungle - GNR'

print(f'Integer value is %d' % Integer)
print(f'Float value is %f' % Float)
print(f'String value is %s' % String)
print('\n')
'''
Output:
Integer value is 10
Float value is 23.880000
String value is Welcome to Jungle - GNR

'''

print(f'Integer value is %d\nFloat value is %f\nString value is %s' %(Integer, Float, String))
'''
Output:
Integer value is 10
Float value is 23.880000
String value is Welcome to Jungle - GNR
'''

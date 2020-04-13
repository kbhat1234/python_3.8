s1 = 'Welcome to kolte patil raaga '
s2 = "Welcome to python programming"
s3 = "Python's programming is simple and easy"
s4 = '"Welcome to machine learning using python"'
s5 = """\nHi Karthik
how are you doing? how is your work going on
Thanks and Regards
Ashish
"""

s6 = '''\nHi Karthik,
how are you doing? how is work life balance.
Regards
Shiva
'''

# printing strings
print(f's1 is {s1}')
print(f's2 is {s2}')
print(f's3 is {s3}')
print(f's4 is {s4}')
print(f's5 is {s5}')
print(f's6 is {s6}')

# length of strings, includes space for length
s1_len = len(s1)
s2_len = len(s2)
s3_len = len(s3)
s4_len = len(s4)
s5_len = len(s5)
s6_len = len(s6)

# printing the length of strings
print(f'length of s1 is {s1_len}')
print(f'length of s2 is {s2_len}')
print(f'length of s3 is {s3_len}')
print(f'length of s4 is {s4_len}')
print(f'length of s5 is {s5_len}')
print(f'length of s6 is {s6_len}')

# accessing characters using index in strings
print(f'{s1[0]} is at position s1[0]')
print(f'{s2[6]} is at position s2[6]')
print(f'{s1[-2]} is at position s1[-2]')
print(f'{s1[4:-2]}')
print(f'{s1[0:6]}')
print(f'{s1[0:]}')
print(f'{s1[4:]}')
print(f'{s1[:-7]}')
print(f'{s1[:]}')

# type of variable
print(type(s1))
print(type(s1_len))

# string concatenation
print(f'{s1 + s2}')
print(f'{s1 * 2}')
'''
print(f'{s1 * s2}')
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Strings/PythonStrings.py", line 59, in <module>
    print(f'{s1 * s2}')
TypeError: can't multiply sequence by non-int of type 'str'
'''
print(f'{s2 * 4}')

print(R'C://Python38//PythonPackage')

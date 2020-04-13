# replace() string method
s1 = "c++ is object oriented programming language"
print(f'old string is {s1}')
print(f"new string is {s1.replace('c++', 'Java')}")
'''
Output:
old string is c++ is object oriented programming language
new string is Java is object oriented programming language
'''

print(f'old string is {s1}')
print(f"new string is {s1.replace('c++', 'Java Java')}")
'''
Output:
old string is c++ is object oriented programming language
new string is Java Java is object oriented programming language
'''

s2 = "c++ is simple and easy to learn. c++ is oop. c++ is dynamic"
print(f'old string is {s2}')
print(f"new string is {s2.replace('c++', 'java', 1)}")
'''
Output:
old string is c++ is simple and easy to learn. c++ is oop. c++ is dynamic
new string is java is simple and easy to learn. c++ is oop. c++ is dynamic
'''

print(f'old string is {s2}')
print(f"new string is {s2.replace('c++', 'java', 2)}")
'''
Output:
old string is c++ is simple and easy to learn. c++ is oop. c++ is dynamic
new string is java is simple and easy to learn. java is oop. c++ is dynamic
'''
print(f'old string is {s2}')
print(f"new string is {s2.replace('c++', 'java', 3)}")
'''
Output:
old string is c++ is simple and easy to learn. c++ is oop. c++ is dynamic
new string is java is simple and easy to learn. java is oop. java is dynamic
'''
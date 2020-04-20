dic1 = {'name': 'karthik', 'age': 41, 'profession': 'software engineer'}
print(f"name is {dic1.get('name')}")
print(f"age is {dic1.get('age')}")
print(f"profession is {dic1.get('profession')}")
'''
Output:
name is karthik
age is 41
profession is software engineer
'''

# key not present in the dictionary and value not provided
print(f"salary is {dic1.get('salary')}")
'''
Output:
salary is None
'''

# Key not present in the dictionary and value is provided
print(f"gender is {dic1.get('gender', 'Male')}")
'''
Output:
gender is Male
'''
print(f'dic1 is {dic1}')
'''
Output:
dic1 is {'name': 'karthik', 'age': 41, 'profession': 'software engineer'}
'''

# print(dic1['salary']) -> error seen when key is not present
'''
Output:
"C:\Program Files\Python38\python.exe" "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Dictionary/Dictionary-get.py"
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Dictionary/Dictionary-get.py", line 31, in <module>
    print(dic1['salary'])
KeyError: 'salary'
'''
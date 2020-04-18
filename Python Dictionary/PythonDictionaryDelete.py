dic1 = {}
print(f'dic1 is {dic1}')
'''
Output:
dic1 is {}
'''
dic1['name'] = input('enter name ')
dic1['age'] = int(input('enter age '))
dic1['gender'] = input('enter gender ')
dic1['school'] = input('enter school ')

print(f'dic1 is {dic1}')
'''
Output:
enter name karthik
enter age 41
enter gender Make
enter school dps
dic1 is {'name': 'karthik', 'age': 41, 'gender': 'Make', 'school': 'dps'}
'''

dic1['class'] = 'grade 4'
dic1['section'] = 'A'
dic1['marks'] = 'Grade A'

print(f'dic1 after update is {dic1}')
'''
Output:
dic1 after update is {'name': 'karthik', 'age': 41, 'gender': 'Make', 'school': 'dps', 'class': 'grade 4', 'section': 'A', 'marks': 'Grade A'}
'''
print("Name is %s " % dic1['name'], "\nAge is %d " % dic1['age'], "\nGender is %s " % dic1['gender'], "\nSchool is %s " % dic1['school'],
      "\nClass is %s " % dic1['class'], "\nSection is %s " % dic1['section'], "\nMarks is %s " % dic1['marks'])
'''
Output:
Name is karthik  
Age is 41  
Gender is Make  
School is dps  
Class is grade 4  
Section is A  
Marks is Grade A
'''

# delete elements from dictionary using del keyword
print(f'dic1 before delete elements is {dic1}')
'''
Output:
dic1 before delete elements is {'name': 'karthik', 'age': 41, 'gender': 'Male', 'school': 'dps', 'class': 'grade 4', 'section': 'A', 'marks': 'Grade A'}
'''
del dic1['marks']
print(f'dic1 after deleting is {dic1}')
'''
Output:
dic1 after deleting is {'name': 'karthik', 'age': 41, 'gender': 'Male', 'school': 'dps', 'class': 'grade 4', 'section': 'A'}
'''
del dic1['section']
print(f'dic1 after deleting is {dic1}')
'''
Output:
dic1 after deleting is {'name': 'karthik', 'age': 41, 'gender': 'Male', 'school': 'dps', 'class': 'grade 4'}
'''
del dic1
# print(dic1)
'''
Output:
    print(dic1)
NameError: name 'dic1' is not defined
'''
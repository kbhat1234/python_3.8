birth_year = input('Birth year please ')
age = 2020 - int(birth_year)
print(f'Age is {age} \nBirth year is {birth_year}')
print(f'Age is of type {type(age)} \nbirth_year is of type {type(birth_year)}')

weight_lbs = input('weight in pounds please ')
weight_kgs = float(weight_lbs) * 0.45
print(f'Weight in lbs(pounds):{weight_lbs}  \nWeight in kgs(kilograms):{weight_kgs}')

a = 'strings'
print(f'a type is of {type(a)} \na valaue is {a}')

"""
integer to float using float(b)
"""
b = 10
print(f'value of b is {float(b)}')

"""float to integer using int(c)"""
c = 10.23
print(f'value of c is {int(c)}')

"""string to integer using int(d)"""
d = '12345'
print(f'value of d is {int(d)}')

"""integer to boolean using bool(e), will give True"""
e = 1
print(f'value of e is {bool(e)}')

"""integer to boolean using bool(e), will give False"""
e = 0
print(f'value of e is {bool(e)}')

"""string to float using float(f)"""
f = '112.6566'
print(f'value of f is {float(f)}')
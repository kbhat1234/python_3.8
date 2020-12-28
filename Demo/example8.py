list1 = [10, 20, 30, 40, 50]

for i in list1:
    print(i)
    if i == 30:
        break

#  single line comment
"""
Multiline comment
"""

a = 10
str1 = 'karthik'
b = 10.33
c = 10 + 4j

print(f'{a} {str1} {b} {c}')

print(f'{a}->{type(a)} {str1}->{type(str1)} {b}->{type(b)} {c}->{type(c)}')

print(f'{a}->{type(a)}->{str(a)}->{type(str(a))}')
print(f'{str1}->{type(str1)}->{list(str1)}->{type(list(str1))}')

print('karthik bhat')
print(type('karthik bhat'))


a1 = 10
a2 = a1

print(f'{a1} {a2}')



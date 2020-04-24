days1 = {'monday', 'tuesday', 'wednesday', 'thursday'}
days2 = {'monday', 'tuesday', 'saturday', 'sunday'}

print(f'days1 is {days1}')
print(f'days2 is {days2}')

# using the - (substraction) operator
d1 = days1 - days2
print(f'"(days1 - days2)" is {d1}, length is {len(d1)}')

'''
Output:
"(days1 - days2)" is {'thursday', 'wednesday'}, length is 2
'''

d2 = days2 - days1
print(f'"(days2 - days1)" is {d2}, length is {len(d2)}')
'''
Output:
"(days2 - days1)" is {'saturday', 'sunday'}, length is 2
'''

# using difference() method
s1 = {23, 98, 28, 11, 46}
s2 = {46, 23, 89, 88, 99}
print(f's1 is {s1}')
print(f's2 is {s2}')
'''
Output:
s1 is {23, 98, 28, 11, 46}
s2 is {46, 23, 89, 88, 99}
'''

d3 = s1.difference(s2)
print(f'"s1.difference(s2)" is {d3}')
'''
Output:
"s1.difference(s2)" is {98, 28, 11}
'''

d4 = s2.difference(s1)
print(f'"s2.difference(s1)" is {d4}')
'''
Output:
"s2.difference(s1)" is {89, 88, 99}
'''
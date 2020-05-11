def func1():
    a = 20  # local scope of variable a
    a += 2
    print(f'value of "a" variable inside func1() definition is {a}')


a = 10  # global scope of variable a
print(f'value of "a" variable outside func1() is {a}')
func1()
'''
Output:
value of "a" variable outside func1() is 10
value of "a" variable inside func1() is 22 
'''

def func1(*names):
    print('------printing arguments passed-------')
    for name in names:
        print(name, end=' ')


def func2(*names):
    print(f'\ntype of argument passed is {type(names)}')


func1('karthik', 'ishani', 'kaustubh', 'raagavi')
'''
Output:
------printing arguments passed-------
karthik ishani kaustubh raagavi 
'''

func2('karthik', 'kaustubh')
'''
Output:
type of argument passed is <class 'tuple'>
'''

func1('karthik', 23373, 'bhat', 7634.993)
'''
Output:
------printing arguments passed-------
karthik 23373 bhat 7634.993
'''

func2(22232, 377346.89978)
'''
Output:
type of argument passed is <class 'tuple'>
'''
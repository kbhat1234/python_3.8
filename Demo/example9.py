c = 10
d = 30


def func1():
    print(c)


def func2():
    global c
    c = 20
    print(c)


def func3():
    global c
    global d
    c = c + 1
    d = d - 1
    print(f'{c} {d}')


func1()
func2()
func3()

print(f'{c} {d}')
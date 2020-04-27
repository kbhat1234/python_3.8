# defining functions here
-
def func1(name):
    l = list(name)
    print(f'hello world {name}')
    print(f'string to list is {l}')
    func2()  # func2() is called by func1()


def func2():
    print('end of program')


def froz_list(list):
    print(f'---frozenset(list)---')
    f1 = frozenset(list)
    print(f'set f1 is {f1}')
    func2()  # func2() is called by froz_list()


def froz_dic(dic):
    print(f'---frozenset(dic)---')
    f2 = frozenset(dic)
    print(f'set f2 is {f2}')
    func2()  # func2() is called by froz_dic()


def froz_tup(tup):
    print(f'---frozenset(tup)---')
    f3 = frozenset(tup)
    print(f'set f3 is {f3}')
    func2()  # func2() is called by froz_tup()


def froz_set(set1):
    print(f'---frozenset(set1)---')
    f4 = frozenset(set1)
    print(f'set f4 is {f4}')
    func2()  # func2() is called by froz_set()


def froz_str(str1):
    print(f'---frozenset(str1)---')
    f5 = frozenset(str1)
    print(f'set f5 is {f5}')
    func2()  # func2() is called by froz_str()


func1('karthik')  # calling function
'''
Output:
hello world karthik
string to list is ['k', 'a', 'r', 't', 'h', 'i', 'k']
end of program
'''

froz_list([10, 20, 30, 40])  # calling function
'''
Output:
---frozenset(list)---
set f1 is frozenset({40, 10, 20, 30})
end of program
'''

froz_dic({2: 'karthik', 'id': 20002, 'apple': 20, 'a': 12})  # calling function
'''
Output:
---frozenset(dic)---
set f2 is frozenset({2, 'apple', 'a', 'id'})
end of program
'''
froz_tup((2, 'a', 'karthik', 334, 55.66))
'''
Output:
---frozenset(tup)---
set f3 is frozenset({2, 'a', 'karthik', 334, 55.66})
end of program
'''

froz_set({2, 5, 9, 4, 11})
'''
Output:
---frozenset(set1)---
set f4 is frozenset({2, 4, 5, 9, 11})
end of program
'''

froz_str('abcdefg')
'''
Output:
---frozenset(str1)---
set f5 is frozenset({'a', 'b', 'g', 'e', 'c', 'f', 'd'})
end of program
'''

st = 'sachin'
func1(st)  # passing string st as argument to the calling function
'''
Output:
hello world sachin
string to list is ['s', 'a', 'c', 'h', 'i', 'n']
end of program
'''

l1 = [20, 30, 40, 23]
froz_list(l1)  # passing list l1 as argument to the calling function
'''
Output:
---frozenset(list)---
set f1 is frozenset({40, 20, 30, 23})
end of program
'''

d = {1: 'apple', 2: 'banana', 'banana': 20, 'apple': 10}
froz_dic(d)  # passing dictionary d as argument to the calling function
'''
Output:
---frozenset(dic)---
set f2 is frozenset({'apple', 1, 2, 'banana'})
end of program
'''

t = (10, 20, 'anil', 'arup')
froz_tup(t)  # passing tuple t as argument to the calling function
'''
Output:
---frozenset(tup)---
set f3 is frozenset({'anil', 10, 20, 'arup'})
end of program
'''

s = {20, 40, 'a', 'z', 'karthik', 45.66}
froz_set(s)  # passing set s as argument to the calling function
'''
Output:
---frozenset(set1)---
set f4 is frozenset({20, 'a', 'z', 40, 45.66, 'karthik'})
end of program
'''

str2 = 'bhat'
froz_str(str2)  # passing string atr2 as argument to the calling function
'''
Output:
---frozenset(str1)---
set f5 is frozenset({'h', 'b', 'a', 't'})
end of program
'''
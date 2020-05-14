import demjson as dj


def dic_display():
    print(f'dic elements is {dic}')
    print(f'"type(dic)" is {type(dic)}')


def tup_display():
    print(f'tup elements is {tup}')
    print(f'"type(tup)" is {type(tup)}')


def li_display():
    print(f'li elements is {li}')
    print(f'"type(li)" is {type(li)}')


def str_display():
    print(f'str1 is {str1}')
    print(f'"type(str1)" is {type(str1)}')


# dictionary dic
dic = {
    'name': 'karthik',
    'age': 40,
    'gender': 'male',
    'salary': 5666367.99,
    'phone no': 9886867677
}
dic_display()
'''
Output:
dic elements is {'name': 'karthik', 'age': 40, 'gender': 'male', 'salary': 5666367.99, 'phone no': 9886867677}
"type(dic)" is <class 'dict'>
'''

en_dic = dj.encode(dic)
print(f'encoded data is \n{en_dic}')
print(f'"type(en_dic)" is {type(en_dic)}')
'''
Output:
encoded data is 
{"age":40,"gender":"male","name":"karthik","phone no":9886867677,"salary":5666367.99}
"type(en_dic)" is <class 'str'>
'''

# tuple tup
tup = ('karthik', 'a', 20, 239889.00, True, False, None)
tup_display()
'''
Output:
tup elements is ('karthik', 'a', 20, 239889.0, True, False, None)
"type(tup)" is <class 'tuple'>
'''

en_tup = dj.encode(tup)
print(f'encoded data is \n{en_tup}')
print(f'"type(en_tup)" is {type(en_tup)}')
'''
Output:
encoded data is 
["karthik","a",20,239889.0,true,false,null]
"type(en_tup)" is <class 'str'>
'''

# list li
li = ['karthik', 'a', 2323, 367674.88, True, False, None]
li_display()
'''
Output:
li elements is ['karthik', 'a', 2323, 367674.88, True, False, None]
"type(li)" is <class 'list'>
'''

en_li = dj.encode(li)
print(f'encoded data is \n{en_li}')
print(f'"type(en_li)" is {type(en_li)}')
'''
Output:
encoded data is 
["karthik","a",2323,367674.88,true,false,null]
"type(en_li)" is <class 'str'>
'''

# string str1
str1 = 'welcome to python programming'
str_display()
'''
Output:
str1 is welcome to python programming
"type(str1)" is <class 'str'>
'''

en_str1 = dj.encode(str1)
print(f'encoded data is \n{en_str1}')
print(f'"type(en_str1)" is {type(en_str1)}')
'''
Output:
encoded data is 
"welcome to python programming"
"type(en_str1)" is <class 'str'>
'''
import demjson as dj

dic1 = {
    'name': 'karthik',
    'age': 40,
    'gender': 'male',
    'salary': 433434
}

en_dic = dj.encode(dic1)
print(f'encoded data (JSON string object) is \n{en_dic}')
print(f'type(en_dic) is {type(en_dic)}')
'''
Output:
encoded data (JSON string object) is 
{"age":40,"gender":"male","name":"karthik","salary":433434}
type(en_dic) is <class 'str'>
'''

de_dic = dj.decode(en_dic)
print(f'decoded data (Python dictionary object) is \n{de_dic}')
print(f'type(de_dic) is {type(de_dic)}')
'''
Output:
decoded data (Python dictionary object) is 
{'age': 40, 'gender': 'male', 'name': 'karthik', 'salary': 433434}
type(de_dic) is <class 'dict'>
'''

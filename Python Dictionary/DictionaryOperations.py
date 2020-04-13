from filecmp import cmp

dic = {'name': 'arijith', 'roll no': 66363,
       'address': 'kolte patil raaga apartments, b502, 5th floor, yelahanka main road, kannuru, bangalore 562149'}
print(f"name -> {dic['name']}")
print(f"roll no -> {dic['roll no']}")
print(f"address -> {dic['address']}")
print(f'dic is {dic}')
print(dic.keys())
print(dic.values())
dic2 = dic.copy()
print(f'dic2 is {dic2}')
dic3 = dic
print(f'dic3 is {dic3}')
dic3.clear()
print(f'dic3 is {dic3}')
g = dic2.get('roll no')
print(g)
print(dic2.items())
dic2.pop('name')
print(dic2)
dic2.popitem()
print(dic2)
dic2.popitem()
print(dic2)
dic2.setdefault('name')
print(dic2)
dic2.popitem()
print(dic2)

d1 = {'name': 'karthik', 'roll no': 3433, 'address': 'Bangalore', 'phone no': 9886867677, 'salary': 234243.22}
print(dic)
print(d1)
d1.update(dic)
print(d1)
print(d1['roll no'])
print(d1.items())
print(d1.get('phone no'))
d2 = d1.copy()
print(d2)

d1.pop('address')
print(d1)
l = len(d1)
print(l)

d1.popitem()
print(d1)

print(d1.keys())
print(d1.values())

print(d1.fromkeys(d2))

print(type(d2['name']))
print(type(d2['roll no']))
print(type(d2['address']))
print(type(d2['phone no']))
print(type(d2['salary']))
print(str(d2))
p = d2.popitem()
print(str(p))

del d2['roll no']
print(d2)
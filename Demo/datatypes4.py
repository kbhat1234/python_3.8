dic1 = {1: 'karthik', 2: 'rini', 3: 'ishani', 4: 'kaustubh'}

print(type(dic1))
print(dic1)

print(dic1[1])
print(dic1.keys())
print(dic1.values())

dic2 = dic1.copy()
print(dic2)
print(dic2.get(2))
print(dic2.pop(3))
print(dic2.items())

dic2.clear()
print(dic2)
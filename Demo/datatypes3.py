tup = (10, 30, 'karthik', "KARTHIK", '''Karthik Bhat''', 34.55, 3 + 4j)
print(type(tup))
print(tup)

print(tup[0])
print(tup[:])
print(tup[2:])
print(tup[:4])

print(tup * 2)
print(tup + tup)

tup[2] = 'abc'
print(tup)

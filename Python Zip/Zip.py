name = ['karthik', 'rini', 'ishani', 'kaustubh']
age = [41, 39, 10, 2]
data = zip(name, age)
m = list(data)
print(list(data))
a, b = zip(*m)
print(a)
print(b)

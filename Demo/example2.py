list1 = ['karthik', 2000, 20.345, "rini das bhat"]
print("list1 is as follows: ", list1)

print(list1.append('ishani'))
print(list1)
print(list1[0:])
print(list1[3:5])
print(list1[:5])
print(list1[:])
print(list1[-1])
print(list1[-3])

for i in list1:
    print(i)

list2 = []
print(list2)
list2 = list1.copy()
print(list2)

list3 = []
list3 = list2
print(list3)

list2.clear()
print(list2)

list2.insert(1, 'kaustubh')
print(list2)
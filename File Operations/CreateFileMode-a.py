fp1 = open("new.txt", 'r')
print(fp1.tell())

content = fp1.read()
print(content)
print(fp1.tell())
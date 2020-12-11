fp = open('a2.txt', "w")
fp.write('welcome to jungle')
print(fp)
if fp:
    print('file created successfully')
fp.close()


fp1 = open("a2.txt", "a")
fp1.write('python programming')
fp1.close()
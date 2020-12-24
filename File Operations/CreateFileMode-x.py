# create a file with file mode 'x'
# It creates a new file with the specified name. It file name does not exists, it creates a new file.

'''fc1 = open('new.txt', 'x')
if fc1:
    print('file is created', fc1.fileno())
fc1.close()
'''

fc1 = open('new.txt', 'a')
if fc1:
    print('file is appended', fc1.fileno())
fc1.close()

fc1 = open('new.txt', 'w')
if fc1:
    fc1.write('abcd ')
    print('file is written', fc1.fileno())
fc1.close()

fc1 = open('new.txt', 'r')
if fc1:
    a1 = fc1.read(4)
    print('file is been read', a1, fc1.fileno())
fc1.close()

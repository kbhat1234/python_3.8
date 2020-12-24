fp1 = open("new.txt", 'r')
if fp1:
    print("file is opened for reading")
    content = fp1.read(2)
    print("contents of the file is", content)
    print("file pointer is at position", fp1.tell())
    fp1.seek(10, 0)
    print("file pointer is at position", fp1.tell())
fp1.close()

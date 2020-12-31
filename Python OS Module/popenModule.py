import os as o

#  fd = "abcd.py"

#  file write
fp = open(fd, "w")
fp.write("This is sample data")
fp.close()

#  file read
fp = open(fd, "r")
text = fp.read()
print(text)
fp.close()

fp = o.popen(fd, "w")
fp.write("welcome to jungle")
fp.close()

fp = o.popen(fd, "r")
text1 = fp.read()
print(text1)
fp.close()




import os as o

try:
    #  if file does not exist, then throw IO error
    filename = "rmdirModule.py"
    f = open(filename, 'w')
    r = f.read()
    f.close()

except IOError:
    print(o.error)
    print("problem in reading " +filename)

'''
Output:
<class 'OSError'>
problem in reading rmdirModule.py
'''

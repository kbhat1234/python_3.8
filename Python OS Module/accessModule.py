import os as o

path1 = o.access("file4.txt", o.F_OK)
print("Exist path:", path1)

# Checking access with os.R_OK
path2 = o.access("file4.txt", o.R_OK)
print("It access to read the file:", path2)

# Checking access with os.W_OK
path3 = o.access("file4.txt", o.W_OK)
print("It access to write the file:", path3)

# Checking access with os.X_OK
path4 = o.access("file4.txt", o.X_OK)
print("Check if path can be executed:", path4)

'''
Output:
Exist path: True
It access to read the file: True
It access to write the file: False
Check if path can be executed: True
'''
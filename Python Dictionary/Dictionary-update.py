dic = {'fname': 'karthik', 'lname': 'bhat', 'idno': 34242432, 'aadhaar_no': 'ajppb4129b'}
print(f'dic is {dic}')
'''
Output:
{'fname': 'karthik', 'lname': 'bhat', 'idno': 34242432, 'aadhaar_no': 'ajppb4129b'}
'''

# update the dictionary
dic.update({'age': 41})  # updating the dic with new key and value
dic.update({'idno': 54321})  # updating value of dic with existing key
dic.update({'fname': 'ishani', 'gender': 'Female'})  # updating multiple values of given key

print(f'dic after update is {dic}')
'''
Output:
dic after update is {'fname': 'ishani', 'lname': 'bhat', 'idno': 54321, 'age': 41, 'gender': 'Female'}
'''
# updating with another dictionary object
d1 = {1: 100, 2: 200, 3: 300}
print(f'd1 is {d1}')
'''
Output:
d1 is {1: 100, 2: 200, 3: 300}
'''
d2 = {2: 400}
d1.update(d2)  # passing d2 dictionary
print(f'd1 after update is {d1}')
'''
Output:
d1 after update is {1: 100, 2: 400, 3: 300}
'''
fname = 'karthik'
lname = "bhat"
roll_no = '2376'
aadhaar = 327332333
percentage = 97.3
ssn = 24662647324726443242344354353543534543535435345353453454535435345342523325453453534535235

print(f'{fname} \t{lname} \t{roll_no} \t{aadhaar} \t{percentage} \t{ssn}')
print(type(aadhaar))
print(type(percentage))
print(type(ssn))
"""
Output:
karthik 	bhat 	2376 	327332333 	97.3 	24662647324726443242344354353543534543535435345353453454535435345342523325453453534535235
<class 'int'>
<class 'float'>
<class 'int'>
"""

message = """
Hi Karthik,
    how are you doing? how is your work going on? let me know when we can meet up.
regards
Naveen
"""

print(message)
"""
Output:
Hi Karthik,
    how are you doing? how is your work going on? let me know when we can meet up.
regards
Naveen
"""

address = 'Kolte patil raaga apartment, \
B502, 5th floor\
Yelahanka main road, Kannuru, \
Bangalore - 562149'

print(address)
"""
Output:
Kolte patil raaga apartment, B502, 5th floorYelahanka main road, Kannuru, Bangalore - 562149
"""

# Boolean literals - True, False
is_enabled = True
print(is_enabled)
"""
Output:
True
"""

is_checked = False
print(is_checked)
"""
Output:
False
"""

# special Literals - None
a = 10
b = None

print(a)
print(b)

"""
Output:
10
None
"""

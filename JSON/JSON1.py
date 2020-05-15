import json as j
import collections as c

obj = '{"userId": 1, "firstName": "Krish", "lastName": "Lee", "phoneNumber": "123456", "emailAddress": "krish.lee@learningcontainer.com"}'

print(obj)
print(type(obj))
a1 = j.loads(obj)
print(a1)
print(type(a1))

print(j.dumps(a1, indent=3, sort_keys=True))

with open('json files/sample.json', 'r') as rf:
    a1 = j.load(rf)
    print(j.dumps(a1, indent=5, sort_keys=True))
    rf.close()

with open('json files/dic1.json', 'r') as rf:
    a2 = j.load(rf)
    print(j.dumps(a2, indent=3, sort_keys=False))
    rf.close()

d1 = c.defaultdict(int)
print(d1)
print(type(d1))
d1['age'] = 30
d1['number'] = 9886867677
print(d1)

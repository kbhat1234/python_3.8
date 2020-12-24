'''
Data types in python
'''

a = 10
b = 20

c = a + b
print("Sum is ", +c)
print(type(a), type(b), type(c))
print("now type casting the sum c to string ", str(c))
print(type(str(c)))

d = 10.25
e = 4.65

f = d - e
print("Diff is ", +f)
print(type(d), type(e), type(f))
print("now type casting the diff f to string ", str(f))
print(type(str(f)))

str1 = "Welcome to "
str2 = "Python "

print("Full concatenated string is ", str1+str2)
print("Hello, ", str1)
print("Hello, ", str2)

print(str1*2)
print(str1[0:4])
print(str1[4:])
print(str1[0:])
print(str1[:])


def StringOperations1():
    print("Full concatenated string is ", str1 + str2)
    print(str1*4)
    print((str1*4)*2)
    print("Hello, ", str1)
    print("Hello, ", str2)


def StringOperations2():
    print(str1 * 2)
    print(str1[0:4])
    print(str1[4:])
    print(str1[0:])
    print(str1[:])
    StringOperations1()


def IsInstance():
    # isinstance() checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
    print(isinstance(str1, str))
    print(isinstance(f, int))
    print(isinstance(c, float))
    print(isinstance(str2, (int, float, str)))
    print(isinstance(str(f), (int, float, str)))
    print(isinstance(str(f), int))
    print(isinstance(str(f), float))
    print(isinstance(str(f), str))
    StringOperations1()
    StringOperations2()

# StringOperations1()
# StringOperations2()
# IsInstance()

s1 = "Karthik"
s2 = "Rini Das Bhat"

print(s1 in s2)
print(s1 not in s2)

print("Bhat" in s1)
print("Bhat" in s2)
marks = int(input('enter the marks here '))

if marks > 85 and marks <= 100:
    print('Congrats you have scored grade A')
elif marks > 60 and marks <= 85:
    print('You have scored grade B')
elif marks > 50 and marks <= 60:
    print('You have scored grade C')
elif marks > 40 and marks <= 50:
    print('You have scored grade D')
else:
    print('Fail you cannot go to next class')

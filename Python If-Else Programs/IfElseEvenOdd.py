num = int(input('enter any number here '))

if num % 2 == 0:
    print('number is even')
else:
    print('number is odd')

if num > 10:
    num += 2
    print(f'{num}')
else:
    num -= 2
    print(f'{num}')
weight = int(input('Enter the weight: '))
unit = input('(L or l)bs or (K or k)g: ')

"""
use functions lower(), upper(), casefold(), capitalize()
print(unit.casefold())
print(unit.lower())
print(unit.upper())
print(unit.capitalize()
"""
if unit == 'L' or unit == 'l':
    converted = weight * 0.45
    print(f'You are {converted} Kilos')
elif unit == 'K' or unit == 'k':
    converted = weight / 0.45
    print(f'You are {converted} Pounds')
else:
    print('Invalid input')
print(f'End of the program')

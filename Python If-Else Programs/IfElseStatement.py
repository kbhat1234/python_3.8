is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink lot of water, else you will dehydrate")

elif is_cold:
    print("It's a cold day")
    print("wear winter clothes")

else:
    print("what a lovely day")

print("Enjoy your day")

is_Corona_Alive = True
# is_Corona_Alive = False
eat = int(input(f'How many times in a day did you eat during lock down? '))
drink = int(input(f'How many hours in a day did you spend on drinks during lock down? '))
code = int(input(f'How many hours did you code for your company during lock down? '))
work_for_wife = int(input(f'How many hours did you help for wife at house during lock down? '))
sleep = int(input(f'How many hours did you sleep on day during lock down? '))

print(f'Eating {eat} \nDrinking {drink} \nCoding {code} \nWorking for wife {work_for_wife} \nSleep {sleep}')

if is_Corona_Alive:
    print(f'Eat, drink, open the code, work for wife, and sleep')

else:
    print(f'Corona is gone out of india')

print("End of program")

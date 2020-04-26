# defining the function
def Sum(p, q):
    return p + q


def display():
    print(f'a is {x}')
    print(f'b is {y}')
    print(f'Sum of {x} and {y} is {Sum(x, y)}')


# taking input from user
x = int(input('enter x '))
y = int(input('enter y '))

# calling function with parameters x and y
Sum(x, y)  # function Sum passes x and y value to function definition

# calling display() function to print the Sum
display()

print('--------------------------------------------------------------------------------------')


def hello(name):
    print(f'Hi {name}')


def list_operation(list):
    print(f'List index of element 9 is {list.index(9)}')


list1 = [20, 34, 23, 33, 79, 9]
hello('KARTHIK')
list_operation(list1)
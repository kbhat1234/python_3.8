is_checked = False

a = 25
b = 1

if is_checked == 1:
    print(f'a & b (AND) is {a & b}')
else:
    print('bitwise AND not executed')

if is_checked == 0:
    print(f'a | b (OR) is {a | b}')
else:
    print('bitwise OR not executed')

if is_checked == 1:
    print(f'a ^ b (XOR) is {a ^ b}')
else:
    print('bitwise XOR not executed')

if is_checked == 0:
    print(f'~a (NOT) is {~a}')
else:
    print('bitwise NOT not executed')

# binary number is appended with 0's at the end
if is_checked == 1:
    print(f'a << b (Left shift) is {a << b}')
else:
    print('bitwise << not executed')

# the right side bits are removed
if is_checked == 0:
    print(f'a >> b (Right shift) is {a >> b}')
else:
    print('bitwise >> not executed')
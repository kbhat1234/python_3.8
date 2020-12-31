import statistics as s

x = 0b101011
y = 0x12d
z = 100
p = 0o215

a = 3 + 3.56j

print(a)
print(f'{a.real} {a.imag}')

print(x)
print(y)
print(z)
print(p)

l1 = [3, 4, 6, 9, 2]
print(f'{s.mean(l1)}')

l2 = [10, 20, 25, 13, 16, 6]
print(f'{s.median(l2)}')

l3 = [2, 3, 5, 2, 7, 3, 8, 3]
print(s.mode(l3))

print(s.stdev(l3))

print(s.median_low(l3))
print(s.median_high(l3))

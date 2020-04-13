import math
import math as m
from math import pi, e, radians, degrees, sqrt, pow, fabs, log, log10, log2

print(f'using math import with aliasing {m.pi}')
print(f'using math import {math.pi}')
print(f'using from math import pi {pi}')
print('\n')
print(f"euler's value is {math.e}")
print(f"euler's value is {m.e}")
print(f"euler's value is {e}")

print(radians(40))
print(math.sin(2.44))
print(math.cos(2.44))
print(math.tan(2.44))

m.radians()
m.degrees()
m.sin()
m.cos()
m.tan()
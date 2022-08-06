import math
import sys

for _ in range(int(input())):
    x = int(input())
    a = math.floor(x ** (1/2) + 1e-9)
    b = math.floor(x ** (1/3) + 1e-9)
    c = math.floor(x ** (1/6) + 1e-9)
    print(a, b, c, file=sys.stderr)
    print(a + b - c)

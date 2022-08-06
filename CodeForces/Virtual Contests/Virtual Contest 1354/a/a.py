import math

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a <= b:
        print(b)
    elif c <= d:
        print(-1)
    else:
        remaining = a - b
        cycles = math.ceil(remaining / (c - d))
        print(b + cycles * c)

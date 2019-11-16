import math

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a >= b:
        c2 = c - (a - b)
        if c2 < 0:
            minA = a
        else:
            b2 = a + c2 // 2
            a2 = a + c2 - (c2 // 2)
            if a2 == b2:
                a2 += 1
            minA = a2
    else:
        c2 = c - (b - a)
        if c2 <= 0:
            minA = b + 1
        else:
            b2 = b + c2 // 2
            a2 = b + c2 - (c2 // 2)
            if a2 == b2:
                a2 += 1
            minA = a2
    
    # print(minA)
    print(max(0, a + c - minA + 1))

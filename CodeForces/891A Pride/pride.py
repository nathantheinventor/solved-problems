from fractions import gcd

input()
data = [int(x) for x in input().split()]
for a, b in zip(data, data[1:]):
    if gcd(a, b) == 1:
        print(len(data) - data.count(1))
        break
else:
    g = data[0]
    for x in data:
        g = gcd(g, x)
    if g != 1:
        print(-1)
    else:
        raise Exception()
from fractions import gcd
tmp = set([])
for i in range(1, 1000):
    for j in range(1, 1000):
        g = gcd(i, j)
        tmp.add((i // g, j // g))
ans1 = 0
ans2 = 0
for x, y in sorted(tmp, key=lambda x: x[0] + x[1])[:100000]:
    ans1 += x
    ans2 += y
print(ans1, ans2)
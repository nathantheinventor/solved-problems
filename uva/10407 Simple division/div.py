from fractions import gcd

s = [int(x) for x in input().split()][:-1]
while len(s) > 0:
    s = list(set(s))
    for i in range(len(s)- 1, -1, -1):
        s[i] -= s[0]
    g = abs(s[1])
    if len(s) > 2:
        for i in s[2::]:
            g = gcd(g, abs(i))
    print(g)
    tmp = input()
    s = [int(x) for x in tmp.split()][:-1]
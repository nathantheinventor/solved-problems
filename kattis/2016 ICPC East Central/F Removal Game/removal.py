from fractions import gcd

s = input()
while s != "0":
    data = [int(x) for x in s.split()[1:]]
    ans = 0
    data2 = [min([gcd(i, j) for j in data]) for i in data]
    print(sum(data2) - max(data2))
    s = input()
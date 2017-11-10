def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    return int(x)

for _ in range(1):
    s = input().split()
    m = {s[-1]: 1}
    mult = 1
    for i in range(1, int(s[0])):
        mult *= int(s[-i * 2])
        m[s[-i * 2 - 1]] = mult
    x = int(input())
    type1 = s[1]
    type2 = s[3]
    n1 = round(x / m[type1])
    n2 = x // m[type1]
    n3 = x % m[type1]
    n3 = round(n3 / m[type2])
    if n3 == int(s[2]):
        n2 += 1
        n3 = 0
    print(n1, type1)
    print(n2, type1, n3, type2)
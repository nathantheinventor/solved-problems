MOD = 10 ** 9 + 7
def modInv(x, n = MOD - 2):
    if n < 3:
        return (x ** n) % MOD
    tmp = (modInv(x, n // 2) ** 2) % MOD
    if n % 2 == 1:
        return (tmp * x) % MOD
    return tmp

f = [1]
fi = [1]
cur = 1
for i in range(1,1010):
    cur = (cur * i) % MOD
    f.append(cur)
    fi.append(modInv(cur))

def nCr(n, r):
    return (f[n] * fi[r] * fi[n - r]) % MOD

for _ in range(int(input())):
    n = int(input())
    l = sorted([int(x) for x in input().split()])

    values = {}
    for x in l:
        if x not in values:
            values[x] = 0
        values[x] += 1
    
    cur = 0
    lessThan = {}
    for x in values:
        lessThan[x] = cur
        cur += values[x]
    
    cur = 0
    greaterThan = {}
    for x in sorted(values)[::-1]:
        greaterThan[x] = cur
        cur += values[x]

    ans = 0
    
    # Find num of odd sequences
    for i in range(1, n + 1, 2):
        ans = (ans + nCr(n, i)) % MOD
    
    # Find num of even sequences
    for x in values:
        if values[x] == 1:
            continue
        for j in range(2, values[x] + 1):
            tmp = nCr(values[x], j)
            tmp2 = 0
            for b in range(j - 1):
                a = j - b - 2
                for i in range(min(lessThan[x] + b, greaterThan[x] + a) + 1):
                    if i - b < 0 or i - a < 0:
                        continue
                    tmp2 += nCr(lessThan[x], i - b) * nCr(greaterThan[x], i - a)
            tmp2 %= MOD
            ans = (ans + tmp * tmp2) % MOD
    
    print(ans)

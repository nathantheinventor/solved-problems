# import random, math
def div(x, n):
    while x % n == 0:
        x //= n
    return x
fact = {3: [], 11: [], 13: [], 37: [], 9: [], 27: []}
tmp = 1
for _ in range(1400):
    fact[37].append(div(tmp, 37) % 37)
    fact[13].append(div(tmp, 13) % 13)
    fact[11].append(div(tmp, 11) % 11)
    fact[3].append(div(tmp, 3) % 3)
    fact[9].append(div(tmp, 9) % 9)
    fact[27].append(div(tmp, 27) % 27)
    tmp *= max(1, _)

print(1)
def count2(n, factor):
    count = 0
    tmp = factor
    while tmp <= n:
        count += n // tmp
        tmp *= factor
    return count

def count(n, r, factor):
    return count2(n, factor) - count2(r, factor) - count2(n - r, factor)

def modInv(x, n, m):
    if n < 30:
        return (x ** n) % m
    tmp = pow(x, n // 2, m) ** 2 % m
    if n % 2 == 1:
        tmp = tmp * x % m
    return tmp

def mod(n, r, factor, min):
    if count(n, r, factor) >= min:
        return 0
    else:
        orig = factor
        if min > 1:
            factor = factor ** (min - count(n, r, factor))
        ans = orig ** count(n, r, orig) * fact[factor][n % factor ** 2]
        ans *= modInv(fact[factor][r % factor ** 2], factor - 2, factor)
        ans *= modInv(fact[factor][(n - r) % factor ** 2], factor - 2, factor)
        return ans % orig ** min

crt = {(i % 27, i % 11, i % 13, i % 37): i for i in range(142857)}

def solve(n, r):
    mod37 = mod(n, r, 37, 1)
    mod11 = mod(n, r, 11, 1)
    mod13 = mod(n, r, 13, 1)
    mod27 = mod(n, r, 3, 3)
    return [(mod27, mod11, mod13, mod37)]

for _ in range(int(input())):
    n, r = map(int, input().split())
    print(solve(n, r))
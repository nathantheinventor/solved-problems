MOD = 1000000007

fact = [1]
tmp = 1
for i in range(1, 10 ** 5 + 2):
    tmp = i * tmp % MOD
    fact.append(tmp)


def modinv(x, n=MOD-2):
    if n < 3:
        return x ** n % MOD
    tmp = modinv(x, n // 2) ** 2
    if n % 2 == 1:
        tmp = tmp * x
    return tmp % MOD


assert 5 * modinv(5) % MOD == 1

n, t = map(int, raw_input().split())
a = [int(x) for x in raw_input().split()]


def ncr(n, r):
    return fact[n] * modinv(fact[r]) * modinv(fact[n - r]) % MOD


berndp = {}


def bernoulli(r, n):
    """ compute the nth element of the rth row of bernoulli's triangle """
    # print(r, n, end="=>")
    if r not in berndp:
        berndp[r] = {}
    if n in berndp[r]:
        # print(1)
        return berndp[r][n]
    if n >= r:
        # print(2)
        berndp[r][n] = modinv(2, r - 1)
        return berndp[r][n]
    if n <= 0:
        # print(3)
        berndp[r][n] = 0
        return berndp[r][n]
    if n == 1:
        # print(3)
        berndp[r][n] = 1
        return berndp[r][n]
    if n in berndp[r - 1]:
        # print(4)
        berndp[r][n] = berndp[r - 1][n] * 2 - ncr(r - 2, n - 1) % MOD
        return berndp[r][n]
    else:
        # print(5)
        k = min(x for x in berndp[r - 1] if x > n)
        k2 = min([x for x in berndp[r] if x > n] + [10 ** 8])
        if k < k2:
            berndp[r][k] = berndp[r - 1][k] * 2 - ncr(r - 2, k - 1) % MOD
        else:
            k = k2
        tmp = berndp[r][k]
        for j in range(k - 1, n - 1, -1):
            tmp = tmp - ncr(r - 1, j - 1) % MOD
        berndp[r][n] = tmp
        return berndp[r][n]

# for r in range(1, 6):
#     tmp = []
#     for n in range(1, r + 1):
#         tmp.append(bernoulli(r, n))
#     print(*tmp)
#     print("----")


def count(r, m1, m2):
    """ get the number of binary strings with m1 < sum <= m2 """
    if m2 <= m1:
        # print(r,m1,m2,"=>",0)
        return 0
    x1 = bernoulli(r + 1, min(m2 + 1, r + 1))
    # print(x1)
    x2 = bernoulli(r + 1, max(min(m1 + 1, r + 1), 0))
    # print(x2)
    # print(r,m1,m2,"=>",x1 - x2)
    return x1 - x2 % MOD


ans = 0
s = 0
for i, x in enumerate(a):
    s += x
    if i < len(a) - 1:
        s1 = s + a[i + 1]
        ans += (i + 1) * (count(i + 1, t - s1 - 1, t - s) +
                          count(i + 1, t - s1, t - s)) * modinv(2, n - i - 2)
    else:
        ans += (i + 1) * count(i + 1, -1, t - s)
    ans %= MOD

# print(ans)
print(ans * modinv(modinv(2, n)) % MOD)

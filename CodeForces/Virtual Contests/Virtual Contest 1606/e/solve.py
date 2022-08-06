# ans = 0
# n = 6
# for i in range(1,n):
#     for j in range(1,n):
#         for k in range(1,n):
#             for l in range(1,n):
#                 for m in range(1,n):
#                     for o in range(1,n):
#                         for p in range(1,n):
#                             for q in range(1,n):
#                                 for r in range(1,n):
#                                                             x = [i,j,k,l,m,o,p,q,r]
#                                                             if x.count(max(x)) == 1:
#                                                                 ans += 1
# print(ans)

# def combinations(n, k):
#     if n == 1:
#         return [[i] for i in range(1, k+1)]
#     results = []
#     for i in range(1, k + 1):
#         for x in combinations(n - 1, k):
#             results.append([i, *x])
#     return results

# # print(*combinations(3,3), sep="\n")


# def solve(n, k):
#     ans = 0
#     for c in combinations(n, k):
#         while len(c) > 0:
#             if len(c) == 1:
#                 ans += 1
#                 break
#             c = [x - len(c) + 1 for x in c if x >= len(c)]
#     return ans


# for k in range(8, 15):
#     row = []
#     for n in range(1, 6):
#         s = solve(n, k)
#         row.append(s)
#         # print(s)
#     print(*row)

MOD = 998244353

def pow(n, k):
    if k <= 2:
        return n ** k % MOD
    x = pow(n, k // 2) % MOD
    if k % 2 == 1:
        x *= n
    return x % MOD

def last_round(n, x):
    if n <= 1:
        return 0
    if x < n:
        return 0
    return n * (x + 1 - n) * pow((n - 1), (n - 1))

f = [1]
for i in range(2, 501):
    f.append(f[-1] * i)

def ncr(n, r):
    return f[n] // f[r] % MOD

# n, x = 5, 13
def ways(i, j):
    if i == 0 and j == 0:
        return 1
    if j < n - 1:
        return 0
    if j == (n - 1):
        return (n - 1) ** j
    return 0

n, x = map(int, input().split())
if n == 1:
    print(x)
elif n == 2:
    print(x ** 2 - x % MOD)
else:
    ans = 0
    for i in range(n):
        for j in range(x):
            ans += ncr(n, i) * last_round(n - i, x - j) * ways(i, j)
    print((pow(x, n) - ans + MOD) % MOD)
    print(ans)
    # print((pow(x, n) - 292640 + MOD) % MOD)
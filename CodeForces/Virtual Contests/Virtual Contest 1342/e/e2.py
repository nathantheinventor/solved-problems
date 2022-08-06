from math import factorial as f

def ncr(n, r):
    return f(n) // f(r) // f(n - r)

# for n in range(1, 6):
#     for k in range(n):
#         print(n, k, 2 * ncr(n - 1, n - 1 - k) * ncr(n, k) + f(n - k))

def s2(n, k):
    ans = 0
    for i in range(k):
        ans += (-1) ** i * ncr(k, i) * (k - i) ** n
    return ans // f(k)

for n in range(1, 6):
    for k in range(n):
        if k == 0:
            print(n, k, f(n))
        else:
            print(n, k, s2(n, n - k) * 2 * f(n) // f(k))
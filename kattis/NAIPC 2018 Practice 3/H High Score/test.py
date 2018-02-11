import random

def solve(a, b, c):
    return a ** 2 + b ** 2 + c ** 2 + 7 * min(a, b, c)

def fast(a, b, c, d):
    ans = solve(a, b, c)
    ans = max(ans, solve(a + d, b, c))
    ans = max(ans, solve(a, b + d, c))
    ans = max(ans, solve(a, b, c + d))

def slow(a, b, c, d):
    ans = solve(a, b, c)
    for i in range(d + 1):
        for j in range(d + 1):
            k = d - i - j
            if k >= 0:
                ans = max(ans, solve(a + i, b + j, c + k))

for a in range(20):
    print(a)
    for b in range(20):
        for c in range(20):
            for d in range(5, 20):
                if fast(a, b, c, d) != slow(a, b, c, d):
                    print(a, b, c, d)

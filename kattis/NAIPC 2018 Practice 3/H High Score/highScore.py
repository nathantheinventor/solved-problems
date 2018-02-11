def solve(a, b, c):
    return a ** 2 + b ** 2 + c ** 2 + 7 * min(a, b, c)

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = solve(a, b, c)
    if d > 5000:
        ans = max(ans, solve(a + d, b, c))
        ans = max(ans, solve(a, b + d, c))
        ans = max(ans, solve(a, b, c + d))
    else:
        for i in range(d + 1):
            for j in range(d + 1):
                k = d - i - j
                if k >= 0:
                    ans = max(ans, solve(a + i, b + j, c + k))
    print(ans)

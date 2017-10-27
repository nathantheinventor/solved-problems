a, b, c = map(int, input().split())
while True:
    dp = {}
    m = max(b, c)
    for i in range(m + 1):
        dp[-i] = 1
    for i in range(1, a + 1):
        dp[i] = dp[i - b] + dp[i - c]
    ans = dp[a]
    ans = min(200 / (ans - 1), 225 / ans)
    print("{0:6f}".format(ans))
    try:
        a, b, c = map(int, input().split())
    except:
        exit(0)
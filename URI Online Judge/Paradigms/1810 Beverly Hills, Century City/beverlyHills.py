
def solve(n):
    data = []
    days = []
    daysSum = [0]
    s = 0
    for i in range(n):
        t,p,h,d = map(int, input().split())
        data.append((t,p,h,d))
        days.append(d)
        s += d
        daysSum.append(s)
    days2 = [i for i in days]
    for i in range(n - 2, 0, -1):
        days2[i] += days[i + 1]
    
    def elemsStored(x, y):
        return daysSum[y + 1] - daysSum[x]
    
    #dp[i][j] = min cost to produce up through day j on day i
    dp = [[0 for i in range(n)] for j in range(n + 1)]
    dp[0] = [10 ** 9] * n
    started = [[False for i in range(n)] for j in range(n)]
    
    oldH = 0
    for i, (t, p, h, d) in enumerate(data):
        for j in range(i, n):
            dp[i + 1][j] = dp[i][j] + oldH * days[j]
            cost2 = days[j] * p + (t if i == j else 0)
            
            if cost2 <= dp[i + 1][j]:
                dp[i + 1][j] = cost2
                started[i][j] = True
        print(*dp[i + 1])
        oldH = h
    
    ans = sum([dp[i + 1][i] for i in range(n)])
    print(ans)

n = int(input())
i = 1
while n > 0:
    if i != 1:
        print("")
    print("Instancia #{}".format(i))
    i += 1
    solve(n)
    n = int(input())
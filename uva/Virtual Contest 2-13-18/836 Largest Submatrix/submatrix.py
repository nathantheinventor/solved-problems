t = int(input())

for _ in range(t):
    input()
    s = input()
    n = len(s)
    grid = [s] + [input() for _ in range(1, n)]
    dp = []
    for s in grid:
        tmp = 0
        tmp2 = []
        for c in s:
            if c == '1':
                tmp += 1
            else:
                tmp = 0
            tmp2.append(tmp)
        dp.append(tmp2)
    ans = 0
    # [print(*line) for line in grid]
    for i in range(n):
        for j in range(n):
            orig = ans
            for x in range(1, dp[i][j] + 1):
                for y in range(i + 1):
                    # print(x, y)
                    if dp[i - y][j] < x:
                        ans = max(ans, y * x)
                        # print(1)
                        break
                else:
                    ans = max(ans, (i + 1) * x)
                    # print(2)
            # if ans != orig:
            #     print(i,j,ans)
            
    print(ans)
    if _ != t - 1:
        print("")
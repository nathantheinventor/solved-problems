from math import sqrt

n = int(input())
l, w = map(int, input().split())
points = sorted([int(input()) for _ in range(n)])
targets = []
for i in range(n // 2 + 1):
    target = i // 2 *(l / ((n - 2) // 2))
    targets.append(target)
# print(*targets)
dp = [[0 for _ in range(n // 2 + 1)] for _ in range(n // 2 + 1)]
for i in range(n // 2 + 1):
    for j in range(n // 2 + 1):
        # print(i+j, deltax[i+j], deltay[i+j])
        ans = 2 ** 31
        if i == 0 and j == 0:
            ans = 0
        if i > 0:
            ans = dp[i - 1][j] + abs(points[i + j - 1] - targets[j])
        if j > 0:
            tmp = abs(points[i + j - 1] - targets[i] + w * 1j)
            x = points[i + j - 1] - targets[i]
            tmp2 = sqrt(x * x + w * w)
            # assert (tmp == tmp2)
            ans = min(ans, dp[i][j - 1] + tmp2)
        dp[i][j] = ans
# for _ in dp:
#     print(*_, sep="\t")
print(dp[-1][-1])
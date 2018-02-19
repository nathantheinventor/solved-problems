def solve(num, start, end):
    if start == 1 and end == 2:
        return 3
    if end < start:
        return 10 ** 10
    if num == 1:
        dp[num][start][end] = sum(range(start, end + 1))
    elif start == end:
        dp[num][start][end] = start
    elif dp[num][start][end] == -1:
        dp[num][start][end] = min([j + max(solve(num - 1, start, j - 1), solve(num, j + 1, end)) for j in range(start, end + 1)])
    return dp[num][start][end]

dp = [[[-1 for i in range(101)] for j in range(101)] for _ in range(11)]
for _ in range(int(input())):
    k, m = map(int, input().split())
    print(solve(k, 1, m))
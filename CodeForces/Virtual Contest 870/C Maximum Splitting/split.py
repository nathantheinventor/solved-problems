dp = {0: 4, 2: 6, 1: 9, 3: 15}
sum = {0: 1, 2: 1, 1: 1, 3: 2}

def solve(x):
    if x in [4, 6, 9]:
        return 1
    if x == 15:
        return 2
    tmp = dp[x % 4]
    if tmp >= x:
        return -1
    return sum[x % 4] + (x - tmp) // 4

for _ in range(int(input())):
    print(solve(int(input())))
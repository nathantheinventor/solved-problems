dp = {}
seen = []

def maxBefore(x: int) -> int:
    lo, hi = 0, len(seen) - 1
    if hi == -1:
        return 0
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if seen[mid] <= x:
            lo = mid
        else:
            hi = mid
    if seen[hi] <= x:
        return seen[hi]
    return seen[lo]

while True:
    try:
        n = int(input())
    except:
        exit(0)
    ranges = []
    for _ in range(n):
        x, y = map(int, input().split())
        ranges.append((y, x))
    ranges = sorted(ranges)
    dp = {0: 0}
    seen = [0]
    for y, x in ranges:
        ans = dp[maxBefore(y)]
        ans = max(ans, y - x + dp[maxBefore(x)])
        dp[y] = ans
        seen.append(y)
    print(dp[seen[-1]])
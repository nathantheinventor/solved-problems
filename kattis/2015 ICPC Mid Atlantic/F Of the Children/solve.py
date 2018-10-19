def canReach(init):
    
    return True

n = int(input())
while n > 0:
    collected = [0] + [int(input()) for _ in range(n - 2)] + [0]
    adj = [[-1 for _ in range(n)] for _ in range(n)]
    i, j, c = map(int, input().split())
    while i > -1:
        adj[i][j] = c
        adj[j][i] = c
        i, j, c = map(int, input().split())
    lo, hi = 0, 1000000
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if canReach(mid):
            hi = mid
        else:
            lo = mid
    if canReach(lo):
        print(lo)
    else:
        print(hi)
    n = int(input())
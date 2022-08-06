from itertools import permutations

def solve2(perm, k):
    tmp = 0
    m = 0
    for i in range(len(perm)):
        if perm[i] > m:
            tmp = 0
            m = perm[i]
        else:
            tmp += 1
            if tmp == k:
                return m
    return m

def wrong(perm, k):
    return solve2(perm, k) != len(perm)

def solve(n, k):
    ans = 0
    for perm in permutations(range(1, n + 1)):
        if wrong(perm, k):
            ans += 1
    return ans

for i in range(1, 10):
    tmp = []
    for j in range(1, 10):
        tmp.append(solve(i, j))
    print(*tmp)
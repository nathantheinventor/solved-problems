l = []

dp = {}

def chain(x, found = {}):
    print(x, found)
    if x in found:
        return 0
    if x in dp:
        return dp[x]
    found[x] = 1
    dp[x] = chain(l[x], found) + 1
    return dp[x]

for j in range(int(input())):
    dp = {}
    n = int(input())
    l = [-1 for i in range(n + 1)]
    for _ in range(n):
       f, t = map(int, input().split())
       l[t] = f
    ans = 0
    m = 0
    for i in range(1, n + 1):
        c = chain(i, {})
        print(i, c)
        if c > m:
            m = c
            ans = i
        
    print("Case {}: {}".format(j + 1, ans))
    
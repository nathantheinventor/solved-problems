dp = {}
def recurse(x):
    #print(x)
    if x == 5:
        print(dp)
    if x in dp:
        return dp[x]
    dp[x] = (10 ** 100, 0) # preset it to infinity in case of loops
    cost, pickup = 10 ** 100, 0
    for loc, weight in adj[x - 1]:
        cost1, pickup1 = recurse(loc)
        cost1 += weight
        pickup1 += items[x - 1]
        if cost1 < cost:
            cost = cost1
            pickup = pickup1
        elif cost1 == cost:
            pickup = max(pickup, pickup1)
    dp[x] = (cost, pickup)
    return dp[x]

n = int(input())
items = [int(i) for i in input().split()]
dp[1] = (0, items[0])
adj = [[] for i in range(n)]
for i in range(int(input())):
    x, y, z = map(int, input().split())
    adj[x-1].append((y, z))
    adj[y-1].append((x, z))
#print(adj)
cost, pickup = recurse(n)
print(dp)
if cost == 10 ** 100:
    print("impossible")
    #print(cost, pickup)
else:
    print(cost, pickup)
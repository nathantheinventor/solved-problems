n = int(input())
l = [int(x) for x in input().split()]
distinct = []
cur = 0
for i in l:
    cur = max(cur, i + 1)
    distinct.append(cur)

for i in range(n - 1, 0, -1):
    distinct[i - 1] = max(distinct[i - 1], distinct[i] - 1)

ans = sum([a - b - 1 for a, b in zip(distinct, l)])
print(ans)
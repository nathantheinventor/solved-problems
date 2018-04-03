n, u = map(int, input().split())
E = [int(x) for x in input().split()] + [10 ** 10]

ans = -1
k = 0
for i in range(n):
    while E[k + 1] <= E[i] + u:
        k += 1
    if k - i >= 2:
        n = (E[k] - E[i + 1]) / (E[k] - E[i])
        ans = max(ans, n)

print(ans)
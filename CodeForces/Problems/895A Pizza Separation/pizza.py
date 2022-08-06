n = int(input())
l = [int(x) for x in input().split()]

ans = 360
for i in range(n):
    for j in range(i + 1, n):
        ans = min(ans, abs(180 - sum(l[i:j])) * 2)

print(ans)
a, b, c = map(int, input().split())
m = min(a, b)
a -= m
b -= m
ans = m
m = min(max(a, b), c)
ans += m
c -= m
if c > 0:
    ans += c // 2
print(ans * 2)
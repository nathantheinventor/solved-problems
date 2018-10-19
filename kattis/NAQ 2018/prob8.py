n, p, c = map(int, input().split())
cur = 1
pills = []
for _ in range(p):
    t, x, y = map(int, input().split())
    if x / y > cur:
        cur = x / y
        pills.append(t, x, y)


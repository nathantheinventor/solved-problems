n, w = map(int, input().split())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a,b))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a, b = l[i]
        c, d = l[j]
        if c == a:
            continue
        v = (a * d - b * c) / (c - a)
        # print(v)
        if -w <= v <= w:
            print(i, j, v)
            ans += 1

print(ans)
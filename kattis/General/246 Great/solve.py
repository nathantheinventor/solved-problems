n, t = map(int, input().split())
solution = []
cheers = [(1, [1], 1, 1)]
negatives = []
for i in range(n):
    s, d = map(int, input().split())
    if s < 0:
        negatives.append((i + 2, s, d))
    elif d < s:
        cheers.append((d / s, [i + 2], s, d))

for i, s, d in negatives:
    new_cheers = []
    for r, i2, s2, d2 in cheers:
        for c in range(1, int(s2 // -s) + 1):
            s3 = s2 + s * c
            d3 = d2 + d * c
            if s3 == 0:
                continue
            if d3 < s3:
                new_cheers.append((d3 / s3, i2 + [i] * c, s3, d3))
    cheers.extend(new_cheers)

cheers = [(r, tuple(i), s, d) for r, i, s, d in cheers]
ans = 0
for r, i, s, d in sorted(cheers):
    rem = t - ans
    c = rem // s
    for _ in range(c):
        solution.extend(i)
    # print(r, i, s, d, c)
    ans += s * c
    if ans == t:
        break

print(len(solution))
print(*sorted(solution))
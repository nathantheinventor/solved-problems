input()
x = [int(x) for x in input().split()]
ranges = []
mins = {}
maxs = {}
for i, y in enumerate(x):
    mins[y] = mins.get(y, i)
    maxs[y] = i

for y in {*x}:
    if maxs[y] > mins[y] + 1:
        ranges.append((mins[y], maxs[y]))

ranges2 = []
for x, y in sorted(ranges):
    if not len(ranges2):
        ranges2.append([x, y])
    elif ranges2[-1][-1] > x:
        if y > ranges2[-1][-1]:
            ranges2[-1][-1] = y
            ranges2[-1][0] += 1
    else:
        ranges2.append([x, y])

# print(ranges, ranges2)
ans =0
for a, b in ranges2:
    ans += b - a - 1
print(ans)
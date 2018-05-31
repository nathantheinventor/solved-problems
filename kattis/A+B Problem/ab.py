n = int(input())
l = sorted([int(x) for x in input().split()])

counts = {}
sums = {x: 0 for x in range(-100000, 100001)}
for i in l:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
    sums[i * 2] -= 1

for i in l:
    for j in l:
        sums[i + j] += 1

ans = 0
for i in counts:
    ans += counts[i] * sums[i]

print(ans)
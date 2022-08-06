import sys

in_data = sys.stdin.read().split("\n")

n, m = map(int, in_data[0].split())
a = [[1e100 for _ in range(m + 2)]]
for row in in_data[1:n + 1]:
    a.append([1e100, *[int(x) for x in row.split()], 1e100])
a.append([1e100 for _ in range(m + 2)])

bads = []
locations = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        x = a[i][j]
        locations[x] = (i, j)
        if x == 1:
            continue
        if x < min(a[i - 1][j], a[i + 1][j], a[i][j - 1], a[i][j + 1]):
            bads.append((i, j))

def swap_works(i1, j1, i2, j2):
    if i1 == i2 and j1 == j2:
        return False
    if not 0 < i1 <= n:
        return False
    if not 0 < i2 <= n:
        return False
    if not 0 < j1 <= m:
        return False
    if not 0 < j2 <= m:
        return False
    a[i1][j1], a[i2][j2] = a[i2][j2], a[i1][j1]
    ans = True
    deltas = [[i2, j2], [i1, j1]]
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        deltas.append([i1 + di, j1 + dj])
        deltas.append([i2 + di, j2 + dj])
    for i, j in bads + deltas:
        x = a[i][j]
        if x == 1 or x == 1e100:
            continue
        if x < min(a[i - 1][j], a[i + 1][j], a[i][j - 1], a[i][j + 1]):
            ans = False
    a[i1][j1], a[i2][j2] = a[i2][j2], a[i1][j1]
    # if ans and n == 22 and m == 90:
    #     print(i1, j1, i2, j2)
    return ans

def count_swaps():
    ans = 0
    i1, j1 = bads[0]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for di, dj in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                if swap_works(i1 + di, j1 + dj, i, j):
                    ans += 1
    return ans

if len(bads) == 0:
    print(0)
else:
    if n == 22 and m == 90:
        print(bads)
    cnt = count_swaps()
    if cnt:
        print(1, cnt)
    else:
        print(2)


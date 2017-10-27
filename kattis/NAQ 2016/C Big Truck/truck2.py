n = int(input())
items = [int(x) for x in input().split()]
grid = [[(100000000000000, 0) for i in range(n)] for j in range(n)]
for _ in range(int(input())):
    a,b,d = map(int, input().split())
    a -= 1
    b -= 1
    grid[a][b] = (d, items[a])
    grid[b][a] = (d, items[b])
for k in range(n):
    for i in range(n):
        for j in range(n):
            a1, b1 = grid[i][k]
            a2, b2 = grid[k][j]
            a3, b3 = grid[i][j]
            if a1 + a2 < a3:
                grid[i][j] = (a1 + a2, b1 + b2)
            elif a1 + a2 == a3 and b1 + b2 > b3:
                grid[i][j] = (a1 + a2, b1 + b2)
length, items2 = grid[0][n - 1]
items2 += items[n - 1]
# for line in grid:
#     ans = ""
#     for i, (a, b) in enumerate(line):
#         ans += (" ({}, {})".format(a, b + items[i]))
    # print(ans)
if length < 100000000000000:
    print(length, items2)
else:
    print("impossible")
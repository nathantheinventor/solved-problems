ans = 0
board = [int(x) for x in input().split()]
for i in range(14):
    tmp = [x for x in board]
    tmp2 = tmp[i]
    tmp[i] = 0
    for j in range(14):
        tmp[j] += tmp2 // 14
    tmp2 %= 14
    for j in range(1, tmp2 + 1):
        tmp[(i + j) % 14] += 1
    ans = max(ans, sum([x for x in tmp if x % 2 == 0]))
print(ans)
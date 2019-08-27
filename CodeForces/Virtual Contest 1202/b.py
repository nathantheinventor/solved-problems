s = input()
pairs = {a + b: 0 for a in "0123456789" for b in "0123456789"}
for a, b in zip(s, s[1:]):
    pairs[a+b] += 1

def solve(x, y, i, j):
    ans = 20
    for a in range(10):
        for b in range(10):
            if (i + a * x + b * y + x) % 10 == j:
                ans = min(ans, a + b)
            if (i + a * x + b * y + y) % 10 == j:
                ans = min(ans, a + b)

    if ans == 20:
        return -1
    return ans

row4 = []
for x in range(10):
    row3 = []
    for y in range(10):
        row2 = []
        for i in range(10):
            row1 = []
            for j in range(10):
                row1.append(solve(x, y, i, j))
            row2.append(row1)
        row3.append(row2)
    row4.append(row3)

for x in range(10):
    row = []
    for y in range(10):
        ans = 0
        for i in range(10):
            for j in range(10):
                s = f"{i}{j}"
                if pairs[s] > 0:
                    tmp = solve(x, y, i, j)
                    # print(x, y, i, j, tmp, pairs[s])
                    ans += tmp * pairs[s]
                    if tmp == -1:
                        ans = -1
                        break
            else:
                continue
            break
        row.append(ans)
    print(*row)
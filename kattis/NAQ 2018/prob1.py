boards = []
n = int(raw_input())
for _ in range(n):
    board = [[int(x) for x in raw_input().split()] for __ in range(5)]
    boards.append(board)
    if _ != n - 1:
        raw_input()

pos = {x: [] for x in range(3001)}
for i, board in enumerate(boards):
    for j, line in enumerate(board):
        for k, x in enumerate(line):
            pos[x].append((i,j,k))

def solve(order):
    scores = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
    for x in order:
        winners = set()
        for i,j,k in pos[x]:
            scores[i][j][k] = True
            if scores[i][j] == [True, True, True, True, True]:
                winners.add(i)
        if winners:
            return winners

seqs = []

for i, x in enumerate(boards):
    for j, y in enumerate(boards):
        if j <= i:
            continue
        for line1 in x:
            for line2 in y:
                s1 = set(line1)
                s2 = set(line2)
                intersect = s1 & s2
                if intersect:
                    order = list(s1 - intersect) + list(s2 - intersect) + list(intersect)
                    s = solve(order)
                    if i in s and j in s:
                        print i + 1, j + 1
                        exit(0)

print("no ties")
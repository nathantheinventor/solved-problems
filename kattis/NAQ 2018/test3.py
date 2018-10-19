from collections import deque

n, k, s = map(int, input().split())
parents = [-1 for _ in range(n)]
children = [{} for _ in range(n)]
childrenLeft = [0 for _ in range(n)]

for _ in range(k):
    p, c = map(int, input().split())
    p -= 1
    c -= 1
    parents[c] = p
    children[p][c] = 0
    childrenLeft[p] += 1

leaves = [i for i in range(n) if children[i] == []]
startingPoints = {i: 0 for i in range(n)}
skiers = {i: 0 for i in range(n)}
paths = []
for _ in range(s):
    f, t = map(int, input().split())
    startingPoints[f] += 1
    skiers[t] += 1
    paths.append((f, t))

childrenLeft2 = [i for i in childrenLeft]
todo = deque(leaves)
while len(todo) > 0:
    c = todo.popleft()
    if childrenLeft2[c] > 0:
        todo.append(c)
        continue
    p = parents[c]
    if p != -1:
        todo.append(p)
        childrenLeft2[p] -= 1
        skiers[p] += skiers[c] - startingPoints[c]
        children[p][c] = skiers[c] - startingPoints[c]

ans = 0

childrenLeft2 = [i for i in childrenLeft]
todo = deque(leaves)
while len(todo) > 0:
    c = todo.popleft()
    if childrenLeft2[c] > 0:
        todo.append(c)
        continue
    p = parents[c]
    if p != -1:
        todo.append(p)
        childrenLeft2[p] -= 1
        if skiers[c]
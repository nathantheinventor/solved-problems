import random
from datetime import datetime
n, k = map(int, input().split())

grid = [[int(x) - 1 for x in input().split()] for _ in range(k)]

for line in grid:
    if len(set(line)) != n:
        print("no")
        # print("row", line)
        exit(0)

tmp = {i for i in range(n)}
remaining = []

for col in zip(*grid):
    if len(set(col)) != k:
        print("no")
        # print("col", col, set(col))
        exit(0)
    remaining.append(tmp - set(col))
    # print(col, tmp - set(col))

if k == 0:
    remaining = [{i for i in range(n)} for _ in range(n)]

d1 = datetime.now()

for i in range(n - k):
    todo = {i for i in range(n)}
    order = [-1 for _ in range(n)]
    seen = {}
    seen2 = set()
    failed = False
    while todo:
        d2 = datetime.now()
        if (d2 - d1).seconds > .5:
            failed = True
            break
        this = min(todo)
        if remaining[this] - seen2:
            tmp = random.choice(list(remaining[this] - seen2))
            order[this] = tmp
            seen[tmp] = this
            seen2.add(tmp)
            todo.remove(this)
        else:
            for i in remaining[this]:
                todo.add(seen[i])
                del seen[i]
                seen2.remove(i)
    if failed:
        break
    grid.append(order)
    for i in range(n):
        remaining[i].remove(order[i])
    print(*map(lambda x: x + 1, order))

print("------")

for i in range(n - len(grid)):
    order = []
    failed = False
    while len(order) < n:
        d2 = datetime.now()
        if (d2 - d1).seconds > 1:
            failed = True
            break
        order = []
        seen = set()
        for i in range(n):
            possiblilities = remaining[i]
            for j in range(i + 1, n):
                if len(remaining[j] - seen) == 1:
                    x = min(remaining[j] - seen)
                    possiblilities -= {x}
            if possiblilities:
                x = random.choice(list(possiblilities))
                order.append(x)
                seen.add(x)
            else:
                break
    if failed:
        break
    grid.append(order)
    for i in range(n):
        remaining[i].remove(order[i])
    print(*map(lambda x: x + 1, order))

print("------")

for _ in range(n - len(grid)):
    choices = [{j for j in range(n) if i in remaining[j]} for i in range(n)]
    taken = set()
    todo = {i for i in range(n)}
    order = [-1 for _ in range(n)]
    bad = 0
    while todo:
        n1 = min(todo)
        indices = choices[n1] - taken
        if not indices:
            bad += 1
            if bad == 10000:
                taken = set()
                todo = {i for i in range(n)}
                continue
            for index in choices[n1]:
                todo.add(order[index])
                taken.remove(index)
        else:
            index = random.choice(list(indices))
            taken.add(index)
            order[index] = n1
            todo.remove(n1)
    grid.append(order)
    for i in range(n):
        remaining[i].remove(order[i])
    print(*map(lambda x: x + 1, order))

print("yes")
for line in grid:
    print(*map(lambda x: x + 1, line))

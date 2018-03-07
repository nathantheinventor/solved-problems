from collections import deque

n = int(input())
parents = [0, 0] + [int(x) for x in input().split()]
children = [set([]) for _ in range(n + 1)]
for i, p in enumerate(parents):
    children[p].add(i)

q = deque([(0, 1)])
levels = [0 for _ in range(n + 1)]
maxLevel = 0
while len(q) > 0:
    level, node = q.popleft()
    levels[node] = level
    maxLevel = max(maxLevel, level)
    for i in children[node]:
        q.append((level + 1, i))

levels2 = [0 for _ in range(maxLevel + 1)]
for i in levels[1:]:
    levels2[i] += 1

print(sum([i % 2 for i in levels2]))
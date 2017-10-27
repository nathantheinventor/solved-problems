from collections import deque

for _ in range(int(input())):
    m, k = map(int, input().split())
    coins = []
    for _ in range(m):
        x, y = map(int, input().split())
        coins.append((x, y))
    
    grid = [[100000000000000 for i in range(k + 1)] for j in range(k + 1)]
    grid[0][0] = 0
    queue = deque([(0,0)])
    while len(queue) > 0:
        x, y = queue.popleft()
        value = grid[x][y]
        for x0, y0 in coins:
            if x + x0 > k:
                continue
            if y + y0 > k:
                continue
            if grid[x + x0][y + y0] > value + 1:
                grid[x + x0][y + y0] = value + 1
                queue.append((x + x0, y + y0))
    ans = 100000000000000
    for x in range(k + 1):
        for y in range(k + 1):
            if abs(x + y * 1j) == k:
                ans = min(ans, grid[x][y])
    
    if ans == 100000000000000:
        print("not possible")
    else:
        print(ans)
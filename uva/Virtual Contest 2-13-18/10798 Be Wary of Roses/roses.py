from heapq import *

def neighbors(point):
    x, y = point
    return [(x+1,y), (x - 1, y), (x, y - 1), (x,y-1)]

n = int(input())
while n > 0:
    grid = [list(input()) for _ in range(n)]
    grid90 = [[grid[y][n-1-x] for y in range(n)] for x in range(n)]
    grid180 = [s[::-1] for s in grid[::-1]]
    grid270 = [s[::-1] for s in grid90[::-1]]
    actual = []
    for a, b, c, d in zip(grid, grid90, grid180, grid270):
        tmp = []
        for e,f,g,h in zip(a, b, c, d):
            tmp.append('P' if 'P' in [e,f,g,h] else ('R' if 'R' in [e,f,g,h] else '.'))
        actual.append(tmp)
    [print(*s) for s in actual]
    q = []
    heappush(q, (0,n//2, n//2))
    grid = [[100000 for _ in range(n)] for _ in range(n)]
    grid[n //2][n//2] = 0
    
    while len(q) > 0:
        cost, x,y = heappop(q)
        if x == 0 or y == 0 or x == n -1 or y == n - 1:
            print("At most {} rose(s) trampled.".format(cost))
            break
        if cost != grid[x][y]:
            continue
        point = (x,y)
        for x,y in neighbors(point):
            if actual[x][y] == 'R':
                if cost + 1 < grid[x][y]:
                    grid[x][y] = cost + 1
                    heappush(q, (cost + 1, x, y))
            elif actual[x][y] == '.':
                if cost < grid[x][y]:
                    grid[x][y] = cost
                    heappush(q, (cost, x, y))
    
    n = int(input())
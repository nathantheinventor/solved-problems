winner = {"S": "R", "R": "P", "P": "S"}

t = int(input())

for _ in range(t):
    r, c, n = map(int, input().split())
    grid = [list(input()) for _ in range(r)]
    def neighbors(x, y):
        ans = []
        for i, j in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < r and 0 <= j < c:
                ans.append(grid[i][j])
        return ans
    for __ in range(n):
        newGrid = [[" " for __ in range(c)] for __ in range(r)]
        for i in range(r):
            for j in range(c):
                newGrid[i][j] = winner[grid[i][j]] if winner[grid[i][j]] in neighbors(i,j) else grid[i][j]
        grid = newGrid
    for line in grid:
        print("".join(line))
    if _ != t - 1:
        print("")
left = {"N": "W", "E": "N", "S": "E", "W": "S"}
right = {"N": "E", "E": "S", "S": "W", "W": "N"}
move = {"N": -1j, "E": 1, "W": -1, "S": 1j}
dir = {"O": "W", "N": "N", "S": "S", "L": "E"}

n, m, s = map(int, input().split())
while n > 0:
    # get the grid bounded by #s
    grid = [["#"] * (m + 2)]
    for _ in range(n):
        grid.append(["#"] + list(input()) + ["#"])
    grid.append(["#"] * (m + 2))
    
    curPos = 0
    orientation = "N"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] in ("N", "S", "L", "O"):
                orientation = dir[grid[i][j]]
                grid[i][j] = '.'
                curPos = i * 1j + j
    
    ans = 0
    
    for c in input():
        # print(c, curPos, orientation)
        if c == "E":
            orientation = left[orientation]
        elif c == "D":
            orientation = right[orientation]
        elif c == "F":
            curPos += move[orientation]
            new = grid[int(curPos.imag)][int(curPos.real)]
            if new == '#':
                curPos -= move[orientation]
            elif new == "*":
                grid[int(curPos.imag)][int(curPos.real)] = '.'
                ans += 1
    
    print(ans)
    
    n, m, s = map(int, input().split())
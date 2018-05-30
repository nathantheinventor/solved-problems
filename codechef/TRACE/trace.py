for _ in range(int(input())):
    n = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            ans[i][j] = matrix[i][j]
            if i + 1 < n and j + 1 < n:
                ans[i][j] += ans[i + 1][j + 1]
    print(max([max(row) for row in ans]))
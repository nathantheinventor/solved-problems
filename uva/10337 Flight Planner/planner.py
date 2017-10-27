for _ in range(int(input())):
    input()
    k = int(input())
    data = [[0 for i in range(10)] for j in range(k // 100)]
    for j in range(9, -1, -1):
        l = [int(x) for x in input().split()]
        for i, x in enumerate(l):
            data[i][j] = x
    dp = [[100000000 for i in range(12)] for j in range(k // 100 + 2)]
    dp[0][1] = 0
    last = dp[0]
    for i in range(1, k // 100 + 1):
        row = dp[i]
        rowData = data[i - 1]
        for j in range(1,11):
            tmp = last[j] + 20 - rowData[j - 1]
            row[j - 1] = min(row[j - 1], tmp)
            tmp += 10
            row[j] = min(row[j], tmp)
            tmp += 30
            row[j + 1] = min(row[j + 1], tmp)
        
        last = row
        #print(*row)
    print(last[1])
    print("")
    
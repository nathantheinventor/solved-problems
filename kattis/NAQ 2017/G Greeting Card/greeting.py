coord = [2018, -2018, 2018j, -2018j, 1118 + 1680j, 1680 + 1118j, 1118 - 1680j, 1680 - 1118j, -1118 + 1680j, -1680 + 1118j, -1118 - 1680j, -1680 - 1118j]

inputData = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    inputData[a + b * 1j] = 0

ans = 0
for i in inputData:
    for j in coord:
        if i + j in inputData:
            ans += 1
print(ans // 2)
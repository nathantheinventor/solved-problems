s, b = map(int, input().split())
while s > 0:
    soldiers = [[i, i + 2] for i in range(s)]
    soldiers[0][0] = "*"
    soldiers[-1][1] = "*"
    for i in range(b):
        l, r = map(int, input().split())
        l, r = l - 1, r - 1
        left = soldiers[l][0]
        right = soldiers[r][1]
        if "*" != left:
            soldiers[left - 1][1] = soldiers[r][1]
        if "*" != right:
            soldiers[right - 1][0] = soldiers[l][0]
        print(soldiers[l][0], soldiers[r][1])
    print("-")
    s, b = map(int, input().split())
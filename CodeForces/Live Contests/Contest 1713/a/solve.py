for _ in range(int(input())):
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        if x == 0:
            if y > 0:
                ymax = max(ymax, y)
            else:
                ymin = min(ymin, y)
        else:
            if x > 0:
                xmax = max(xmax, x)
            else:
                xmin = min(xmin, x)
    ans = 2 * (-xmin + xmax + ymax - ymin)
    print(ans)

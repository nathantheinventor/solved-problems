for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if b >= a * 2:
        print((x + y) * a)
    else:
        print(min(x, y) * b + abs(y - x) * a)

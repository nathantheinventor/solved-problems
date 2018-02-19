for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        print("impossible")
    else:
        x = int(a / 2 + b / 2)
        y = int(a / 2 - b / 2)
        if x + y == a:
            print(x, y)
        else:
            print("impossible")
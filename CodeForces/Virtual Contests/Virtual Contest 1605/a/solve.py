for _ in range(int(input())):
    a,b,c = map(int, input().split())
    if ((a+c) - b * 2) % 3 == 0:
        print(0)
    else:
        print(1)

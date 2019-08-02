for _ in range(int(input())):
    input()
    x = sorted([int(x) for x in input().split()])[:-1]
    ans = 0
    for i, a in enumerate(x):
        if a > i:
            ans = i
    print(ans)

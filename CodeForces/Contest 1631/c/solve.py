for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 4 and k == 3:
        print(-1)
        continue
    if k < n - 1:
        print(n - 1, k)
        if k != 0:
            print(0, n - 1 - k)
        for i in range(1, n // 2):
            if i != k and n - 1 - i != k:
                print(i, n - 1 - i)
    else:
        print(n - 1, n - 2)
        print(1, n - 3)
        print(0, 2)
        for i in range(3, n // 2):
            print(i, n - 1 - i)
    
for _ in range(int(input())):
    n, k = map(int, input().split())
    k = min(k, 70)
    if n > 2:
        for i in range(k):
            if n == 1:
                break
            elif n == 2:
                n = 1
            elif n % 4 == 0:
                n = n // 2
            else:
                n = n // 2 + 1
    print(1 / n)
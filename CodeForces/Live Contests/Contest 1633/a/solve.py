for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        n2 = (n // 10) * 10
        for i in range(0, 10):
            if (n2 + i) % 7 == 0:
                print(n2 + i)
                break

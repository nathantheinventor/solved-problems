for _ in range(int(input())):
    a, b = input().split()
    a, b = a[::-1], b[::-1]
    print(int(str(int(a) + int(b))[::-1]))
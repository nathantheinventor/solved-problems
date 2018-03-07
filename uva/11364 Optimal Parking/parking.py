for _ in range(int(input())):
    input()
    l = [int(x) for x in input().split()]
    print((max(l) - min(l)) * 2)
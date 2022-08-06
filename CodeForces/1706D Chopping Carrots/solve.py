for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    a2 = [x // k for x in a]
    print(max(0, max(a2) - min(a)))
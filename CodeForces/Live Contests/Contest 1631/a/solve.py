for _ in range(int(input())):
    input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    d = [max(x, y)for x, y in zip(a, b)]
    e = [min(x, y)for x, y in zip(a, b)]
    print(max(d) * max(e))

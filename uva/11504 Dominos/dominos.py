for i in range(int(input())):
    n, m = map(int, input().split())
    l = [False for i in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        l[b] = True
    ans = len([i for i in l if not i])
    print(ans)
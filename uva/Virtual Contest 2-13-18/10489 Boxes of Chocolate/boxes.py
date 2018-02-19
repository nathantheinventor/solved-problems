for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = 0
    for _ in range(k):
        l = [int(x) for x in input().split()[1:]]
        tmp = 1
        for i in l:
            tmp *= i
            tmp %= n
        ans += tmp
    print(ans % n)
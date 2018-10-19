m, n = map(int, input().split())
while (m, n) != (0, 0):
    gems = {}
    for i in range(m):
        s = input().split()
        gems[s[0]] = [int(x) for x in s[1:]]
    ans, m = "", 0
    for gem in gems:
        first = gems[gem][0]
        second = 0
        for gem2 in gems:
            if gem2 != gem and len(gems[gem2]) > n:
                second = max(second, gems[gem2][n])
        if first + second > m:
            ans = gem
            m = first + second
        elif first + second == m and gem < ans:
            ans = gem
    print(ans)
    m, n = map(int, input().split())

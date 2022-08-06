for _ in range(int(input())):
    input()
    s = input()
    ans = -1
    As = [i for i, x in enumerate(s) if x == "a"]
    if len(As) < 2:
        print(-1)
        continue
    for a, b in zip(As, As[1:]):
        if b - a == 1:
            ans = 2
            break
        elif b - a == 2 and ans != 2:
            ans = 3
        elif b - a == 3 and ans != 2 and ans != 3 and s[a + 1] != s[a + 2]:
            ans = 4
    if ans == -1 and len(As) >= 3:
        for a, b in zip(As, As[2:]):
            if b - a == 6 and s[a:b] in ("abbacc", "accabb"):
                ans = 7
                break
    print(ans)

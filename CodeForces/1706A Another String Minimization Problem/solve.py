for _ in range(int(input())):
    n, m = map(int,input().split())
    s = ["B" for _ in range(m)]
    for x in input().split():
        a = int(x) - 1
        b = m - a - 1
        a, b = min(a, b), max(a, b)
        if s[a] == "A":
            s[b] = "A"
        s[a] = "A"

    print("".join(s))
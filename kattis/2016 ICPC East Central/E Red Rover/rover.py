for _ in range(1):
    s = input()
    #print("{} {}".format(s, len(s)))
    ans = len(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            tmp = s.replace(sub, "M")
            ans = min(ans, len(tmp) + len(sub))
    print(ans)

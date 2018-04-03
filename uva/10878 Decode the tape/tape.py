input()
s = input()
while s != "___________":
    s = s[2:-1]
    tmp = 64
    tmp2 = 0
    for c in s:
        if c == "o":
            tmp2 += tmp
        tmp //= 2
        if c == ".":
            tmp *= 2
    # print(tmp2)
    print(chr(tmp2),end="")
    s = input()
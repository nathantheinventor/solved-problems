for _ in range(int(input())):
    if _ != 0:
        input()
    input()
    data = [input()[1:-1] for _ in range(8)]
    input()
    mult = 1
    ans = [0 for _ in range(len(data[0]))]
    for line in data:
        for i, c in enumerate(line):
            ans[i] += ["/", "\\"].index(c) * mult
        mult *= 2
    print("".join(map(chr, ans)))
def is_sorted(s):
    return max(s[0]) < min(s[1])

for _ in range(int(input())):
    input()
    s = input()
    s = [[i + 1 for i, x in enumerate(s) if x == "0"], [i + 1 for i, x in enumerate(s) if x == "1"]]
    steps = []
    c = min(len(s[1]), len(s[0]))
    while c > 0 and not is_sorted(s):
        x = max(s[0])
        i = 0
        for j in range(c):
            if s[0][-j - 1] > s[1][j]:
                i += 1
            else:
                break
        step = s[0][-i:] + s[1][:i]
        steps.append(step)
        s0 = s[1][:i] + s[0][:-i]
        s1 = s[0][-i:] + s[1][i:]
        s = [sorted(s0), sorted(s1)]

    print(len(steps))
    for step in steps:
        print(len(step), *sorted(step))

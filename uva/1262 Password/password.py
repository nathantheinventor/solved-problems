for _ in range(int(input())):
    k = int(input()) - 1
    l1 = [list(input()) for i in range(6)]
    l2 = [list(input()) for i in range(6)]
    l1 = list(zip(*l1))
    l2 = list(zip(*l2))
    common = []
    num = 1
    for i1, i2 in zip(l1, l2):
        tmp = []
        for i in i1:
            if i in i2:
                tmp.append(i)
        tmp = list(set(tmp))
        num *= len(tmp)
        common.append(sorted(tmp))
    if k >= num:
        print("NO")
    else:
        ans = ""
        for l in common[::-1]:
            pos = k % len(l)
            k //= len(l)
            ans += l[pos]
        print(ans[::-1])
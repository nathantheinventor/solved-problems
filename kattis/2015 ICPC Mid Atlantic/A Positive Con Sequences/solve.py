a, b, c, d = map(int, input().split())
while sum((a, b, c, d)) > -4:
    ans = -1
    seq = [a, b, c, d]
    if a == -1:
        if d - c == c - b:
            ans = (b - (c - b))
        elif d // c == c // b:
            ans = (b // (c // b))
        seq[0] = ans
    elif b == -1:
        # print("b")
        if (d - c) * 2 == c - a:
            # print("b arith")
            ans = (c - (d - c))
        elif (d // c) ** 2 == c // a:
            # print("b mult")
            ans = (c // (d // c))
        seq[1] = ans
    elif c == -1:
        if (b - a) * 2 == d - b:
            ans = (d - (b - a))
        elif (b // a) ** 2 == d // b:
            ans = (d // (b // a))
        seq[2] = ans
    elif d == -1:
        if b - a == c - b:
            ans = (c + (c - b))
        elif b // a == c // b:
            ans = (c * (c // b))
        seq[3] = ans
    a, b, c, d = seq
    # print(a, b, c, d)
    diff = b - a
    if 1 <= ans <= 1000000 and a > 0:
        quot = b // a
        if [a, a + diff, a + 2 * diff, a + 3 * diff] == seq:
            print(ans)
        elif [a, a * quot, a * quot ** 2, a * quot ** 3] == seq:
            print(ans)
        else:
            print(-1)
    else:
        print(-1)
    a, b, c, d = map(int, input().split())
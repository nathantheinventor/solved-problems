for _ in range(int(input())):
    input()
    a = [int(x) for x in input().split()]
    last = a[-1]
    ans = 0
    last_count = 1
    for i in range(last_count, len(a) + 1):
        if a[-i] == last:
            last_count = i
        else:
            break
    
    while not all([x == last for x in a]):
        ans += 1
        x = max(0, len(a) - 2 * last_count)
        a[x:-last_count] = a[-last_count:]
        for i in range(last_count, len(a) + 1):
            if a[-i] == last:
                last_count = i
            else:
                break

    print(ans)

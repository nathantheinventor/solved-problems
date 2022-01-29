for _ in range(int(input())):
    n = int(input())
    ks = [int(x) for x in input().split()]
    hs = [int(x) for x in input().split()]
    starts = []
    for k, h in zip(ks, hs):
        starts.append(k - h + 1)
    ranges = []
    for s, e in sorted(zip(starts, ks)):
        if not len(ranges):
            ranges.append((s, e))
        else:
            s1, e1 = ranges[-1]
            if s <= e1:
                ranges[-1] = (s1, max(e1, e))
            else:
                ranges.append((s, e))
    
    # print(ranges)
    ans = 0
    for s, e in ranges:
        n = e - s + 1
        ans += (n * (n + 1)) // 2
    print(ans)
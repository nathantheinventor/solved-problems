import math
import sys

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted([int(x) for x in input().split()])
    init_sum = sum(a)
    delta = init_sum - k
    ans = max(0, delta)
    i = 1
    s = 0
    while ans > 0 and i < len(a):
        s += (a[-i] - a[0])
        delta2 = init_sum - k - s
        # print(delta2, file=sys.stderr)
        cnt = max(0, math.ceil(delta2 / (i + 1)))
        ans2 = i + cnt
        if ans2 <= ans:
            # break
            ans = ans2
        if ans < 0:
            raise Exception("")
        # a2 = a[0] - cnt
        # print(a2, *a[1:-i], *[a2 for _ in range(i)], file=sys.stderr)
        # print(sum([a2, *a[1:-i], *[a2 for _ in range(i)]]), file=sys.stderr)
        # if sum([a2, *a[1:-i], *[a2 for _ in range(i)]]) > k:
        #     x = 0
        #     while True:
        #         x += 1
        i += 1
    print(ans)
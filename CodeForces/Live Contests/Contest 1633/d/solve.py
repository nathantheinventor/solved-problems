import sys

num_ops = {1: 0}
for i in range(1, 1001):
    for x in range(1, i + 1):
        i2 = i + i // x
        num_ops[i2] = min(num_ops.get(i2, 100000), num_ops[i] + 1)

def do_dp(n, c, k):
    found = {0}
    best = [0 for _ in range(k + 1)]

    for ni, ci in zip(n, c):
        found2 = {0}
        best2 = {}
        for x in found:
            if x + ni <= k:
                # if x + ni == 5:
                    # print(x, best[x], ni, ci, file=sys.stderr)
                found2.add(x + ni)
                best2[x + ni] = best[x] + ci
        for k2, v in best2.items():
            best[k2] = max(best[k2], v)
        for x in found2:
            found.add(x)
    #     print("    ", *best, found, file=sys.stderr)

    # print(*n, file=sys.stderr)
    # print(*c, file=sys.stderr)
    # print(best, file=sys.stderr)
    return max(best)

for _ in range(int(input())):
    n, k = map(int, input().split())
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    n = [num_ops[bi] for bi in b]
    if sum(n) <= k:
        print(sum(c))
    elif k == 0:
        print(sum([ci for ci, ni in zip(c, n) if ni == 0] + [0]))
    else:
        print(do_dp(n, c, k))

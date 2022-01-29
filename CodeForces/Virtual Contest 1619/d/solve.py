import sys

def possible(x, p, n):
    covered = [False for _ in range(n)]
    options = []
    for i, l in enumerate(p):
        for j, y in enumerate(l):
            if y >= x:
                covered[j] = True
                options.append(i)
    return all(covered) and len(options) > len({*options})

data = sys.stdin.read().split("\n")
d = -1
def input():
    global d
    d += 1
    return data[d]

for _ in range(int(input())):
    input()
    m, n = map(int, input().split())
    p = [[int(x) for x in input().split()] for _ in range(m)]

    lo, hi = min([min(l) for l in p]), max([max(l) for l in p])
    while hi - lo > 1:
        m = (hi + lo) // 2
        if possible(m, p, n):
            lo = m
        else:
            hi = m
    if possible(hi, p, n):
        print(hi)
    else:
        print(lo)

import sys
import math

def works(values, range_size, required):
    # print("works", values, range_size, required, file=sys.stderr)
    cnt = 0
    for v in range(min(values), max(values) + 1):
        cnt += values.get(v, 0)
        cnt -= values.get(v - range_size - 1, 0)
        if cnt >= required:
            return v - range_size, v
    return False

def get_range(values, required):
    lo, hi = 0, max(values) - min(values)
    while hi - lo > 1:
        m = (hi + lo) // 2
        if works(values, m, required):
            hi = m
        else:
            lo = m
    
    x = works(values, lo, required)
    if x:
        return x
    return works(values, hi, required)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    values = {x: 0 for x in a}
    for x in a:
        values[x] += 1
    needed = math.ceil((n - k) / 2) + k
    x, y = get_range(values, needed)
    cnt = len([b for b in a if x <= b <= y])
    assert cnt >= needed
    print(x, y)
    surplus = 0
    range_start = 1
    range_count = 0
    # print(works(values, 0, 3), file=sys.stderr)
    for i, b in enumerate(a):
        if x <= b <= y:
            surplus += 1
            if surplus > 0 and range_count < k - 1:
                surplus = 0
                print(range_start, i + 1)
                range_start = i + 2
                range_count += 1
        else:
            surplus -= 1
    # assert surplus > 0
    print(range_start, n)
    # print("------", file=sys.stderr)

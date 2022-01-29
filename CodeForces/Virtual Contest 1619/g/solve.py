import bisect
import sys
import time

X = 10 ** 9

def matches(x, k, items):
    a = bisect.bisect_left(items, (x - k, -1))
    b = bisect.bisect_left(items, (x + k, X))
    return [i for x, i in items[a:b]]


data = sys.stdin.read().split("\n")
d = -1
def input():
    global d
    d += 1
    return data[d]

for _ in range(int(input())):
    t0 = time.time()
    input()
    n, k = map(int, input().split())
    ds = [-1 for _ in range(n)]
    
    def root(x):
        while ds[x] > -1:
            x = ds[x]
        return x
    
    def join(x, y):
        rx = root(x)
        ry = root(y)
        if rx == ry:
            return
        if ds[ry] < ds[rx]:
            ds[ry] += ds[rx]
            ds[rx] = ry
        else:
            ds[rx] += ds[ry]
            ds[ry] = rx

    mines = [[int(x) for x in input().split()] for _ in range(n)]
    print(1, time.time() - t0, file= sys.stderr)
    # print(mines, file=sys.stderr)
    cols = {}
    rows = {}
    for i, (x, y, t) in enumerate(mines):
        if x not in cols:
            cols[x] = []
        if y not in rows:
            rows[y] = []
        cols[x].append((y, i))
        rows[y].append((x, i))
    
    print(2, time.time() - t0, file= sys.stderr)
    for x, col in cols.items():
        cols[x] = sorted(col)
    
    for y, row in rows.items():
        rows[y] = sorted(row)
    
    print(3, time.time() - t0, file= sys.stderr)
    vs = set()
    hs = set()

    mines2 = sorted([(x,y,t,i)for i, (x, y, t) in enumerate(mines)])
    for (x,y,t,i) in mines2:
        if len(cols[x]) > 1 and i not in vs:
            for match in matches(y, k, cols[x]):
                join(i, match)
                vs.add(match)
        if len(rows[y]) > 1 and i not in hs:
            for match in matches(x, k, rows[y]):
                join(i, match)
                hs.add(match)
    
    print(4, time.time() - t0, file= sys.stderr)
    explode_times = {}
    for i, (x, y, t) in enumerate(mines):
        r = root(i)
        explode_times[r] = min(explode_times.get(r, X), t)
    times = sorted(explode_times.values())
    # print(times, file=sys.stderr)
    
    print(5, time.time() - t0, file= sys.stderr)
    last = len(times)
    ans = last - 1
    for i in range(len(times)):
        ans = min(ans, max(last - i - 2, times[i]))
    print(ans)
    print(6, time.time() - t0, file= sys.stderr)

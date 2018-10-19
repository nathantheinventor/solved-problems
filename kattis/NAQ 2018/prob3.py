ww, wb, bw, bb, l = map(int, input().split())
e1 = {i: {j: {k: 100000000 for k in range(1, 13)} for j in range(5)} for i in range(5)}
e2 = {i: {j: {k: 100000000 for k in range(1, 13)} for j in range(5)} for i in range(5)}
e3 = {i: {j: {k: 100000000 for k in range(1, 13)} for j in range(5)} for i in range(5)}
e4 = {i: {j: {k: 100000000 for k in range(1, 13)} for j in range(5)} for i in range(5)}
ease = {"W": {"W": e1, "B": e2}, "B": {"W": e3, "B": e4}}
for _ in range(ww):
    fl, fh, *h = map(int, input().split())
    for i in range(12):
        ease["W"]["W"][fl - 1][fh - 1][i + 1] = h[i]
for _ in range(wb):
    fl, fh, *h = map(int, input().split())
    for i in range(12):
        ease["W"]["B"][fl - 1][fh - 1][i + 1] = h[i]
for _ in range(bw):
    fl, fh, *h = map(int, input().split())
    for i in range(12):
        ease["B"]["W"][fl - 1][fh - 1][i + 1] = h[i]
for _ in range(bb):
    fl, fh, *h = map(int, input().split())
    for i in range(12):
        ease["B"]["B"][fl - 1][fh - 1][i + 1] = h[i]
whites = {1, 3, 4, 6, 8, 9, 11}
blacks = {2, 5, 7, 10, 12}
tmp = set()
for w in whites:
    for i in range(0, 88, 12):
        tmp.add(w + i)
whites |= tmp
tmp = set()
for b in blacks:
    for i in range(0, 88, 12):
        tmp.add(b + i)
blacks |= tmp

curCosts = [0 for _ in range(5)]
passage = [int(x) for x in input().split()]
cur = passage[0]
for next in passage[1:]:
    if cur == next:
        continue
    nextCosts = [10000000 for _ in range(5)]
    lower = min(cur, next)
    upper = max(cur, next)
    lowerType = "W" if lower in whites else "B"
    upperType = "W" if upper in whites else "B"
    diff = upper - lower
    if cur < next:
        for lowerFinger in range(5):
            for upperFinger in range(5):
                tmp = curCosts[lowerFinger] + ease[lowerType][upperType][lowerFinger][upperFinger][diff]
                nextCosts[upperFinger] = min(nextCosts[upperFinger], tmp)
    else:
        for lowerFinger in range(5):
            for upperFinger in range(5):
                tmp = curCosts[upperFinger] + ease[lowerType][upperType][lowerFinger][upperFinger][diff]
                nextCosts[lowerFinger] = min(nextCosts[lowerFinger], tmp)
    cur = next
    curCosts = nextCosts

print(min(curCosts))
l, r = 0, 0
tmpL = 1
max = 0
s = input()
cur = 0
for i, c in enumerate(s):
    cur += {"R": +1, "B": -1}[c]
    # print(cur, max, tmpL)
    if cur > max:
        max = cur
        l = tmpL
        r =  i + 1
    if cur < 0:
        cur = 0
        tmpL = i + 2
cur = 0
tmpL = 1
for i, c in enumerate(s):
    cur += {"R": -1, "B": +1}[c]
    # print(cur, max, tmpL)
    if cur > max:
        max = cur
        l = tmpL
        r =  i + 1
    if cur == max and tmpL < l:
        max = cur
        l = tmpL
        r =  i + 1
    if cur < 0:
        cur = 0
        tmpL = i + 2

print(l, r)
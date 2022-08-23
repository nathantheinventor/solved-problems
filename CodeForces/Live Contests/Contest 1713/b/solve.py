def solve():
    input()
    l = [int(x) for x in input().split()]
    m = max(l)
    i = l.index(m)
    last = m
    for j in range(i, len(l)):
        if l[j] > last:
            return False
        last = l[j]
    last = m
    for j in range(i, -1, -1):
        if l[j] > last:
            return False
        last = l[j]
    return True

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")

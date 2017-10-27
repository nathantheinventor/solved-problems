import itertools

s = input()
while s != "0":
    l = [int(x) for x in s.split()[1:]]
    for i in itertools.combinations(l, 6):
        print(*list(i))
    s = input()
    if s != "0":
        print("")
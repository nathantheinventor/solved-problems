def eo(x):
    e, o = x // 3, 2 * (x // 3)
    if x % 3 == 1:
        # print("Case 1")
        e += 1
    if x % 3 == 2:
        # print("Case 2")
        e += 1
        o += 1
    return e, o
    

for testNum in range(1, int(input()) + 1):
    l, h = map(int, input().split())
    e,o = eo(l - 1)
    e2,o2 = eo(h)
    # print(e, o)
    # print(e2, o2)
    print("Case {}:".format(testNum))
    print("Odd =", o2- o)
    print("Even =", e2 - e)
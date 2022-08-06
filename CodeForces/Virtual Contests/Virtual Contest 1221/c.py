for _ in range(int(input())):
    c, m, x = map(int, input().split())
    cm = min(c, m)
    x += m - cm + c - cm
    if x < cm:
        diff = (cm - x) // 3 - 3
        x += 2 * diff
        cm -= diff
    
    while x < cm:
        x += 2
        cm -= 1
    print(max(0, min(cm, x)))

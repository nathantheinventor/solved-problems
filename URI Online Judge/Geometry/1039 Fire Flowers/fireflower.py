r1, x1, y1, r2, x2, y2 = map(int, input().split())
while True:
    c1 = x1 + y1 * 1j
    c2 = x2 + y2 * 1j
    if abs(c2 - c1) <= r1 - r2 + 1e-9:
        print("RICO")
    else:
        print("MORTO")
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
    except:
        break
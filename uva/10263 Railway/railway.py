def nearestPoint(m: complex, p1: complex, p2: complex) -> complex:
    """ Find the point on the line A closest to point m
        A is the line determined by points p1 and p2 """
    # Do a ternary search
    hi, lo = p2, p1
    while abs(hi - lo) > 1e-8:
        m1 = lo + (hi - lo) * 0.3
        m2 = lo + (hi - lo) * 0.6
        if abs(m1 - m) > abs(m2 - m):
            lo = m1
        else:
            hi = m2
    return lo

xm = float(input())
while True:
    ym = float(input())
    m = xm + ym * 1j
    # print(m)
    n = int(input())
    points = []
    for _ in range(n + 1):
        x, y = float(input()), float(input())
        points.append(x + y * 1j)
    
    ans = 0 + 0j
    dist = 10000000
    for p1, p2 in zip(points, points[1:]):
        nearest = nearestPoint(m, p1, p2)
        if abs(nearest - m) < dist:
            dist = abs(nearest - m)
            ans = nearest
    
    print("{:.4f}".format(ans.real))
    print("{:.4f}".format(ans.imag))
    
    try:
        xm = float(input())
    except:
        break
for _ in range(int(input())):
    points = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        points.append(x + y * 1j)
    points = sorted(points, reverse=True, key=lambda x: x.real)
    peak = 0
    last = points[0]
    ans = 0
    for point in points[1:]:
        if point.imag > peak:
            ans += abs(point - last) * (point.imag - peak) / (point.imag - last.imag)
            peak = point.imag
        last = point
    print("{:.2f}".format(ans))
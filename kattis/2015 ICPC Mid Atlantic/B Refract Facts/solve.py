from math import sin, cos, tan, atan, asin, acos, pi

def solve(d, h, x, n1, n2):
    if x == 0:
        return 90
    lo, hi = 0, x
    n = n1 / n2
    while hi - lo > 1e-9:
        mid = (hi + lo) / 2
        phi2 = pi / 2 - atan(h / mid)
        phi1 = pi / 2 - atan(d / (x - mid))
        s = sin(phi1) / sin(phi2)
        if s > n:
            lo = mid
        else:
            hi = mid
    return atan(d / (x - mid)) * 180 / pi

d, h, x, n1, n2 = map(float, input().split())
while d > 0:
    print("{:.2f}".format(solve(d,h,x,n1,n2)))
    d, h, x, n1, n2 = map(float, input().split())
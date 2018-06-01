from decimal import Decimal as D
from fractions import gcd

class complex2:
    def __init__(self, real, imag):
        self.real = D(real)
        self.imag = D(imag)
    
    def __add__(self, other):
        return complex2(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return complex2(self.real - other.real, self.imag - other.imag)

    def __mul__(self, factor):
        factor = D(factor)
        return complex2(factor * self.real, factor * self.imag)
    
    def __truediv__(self, factor):
        factor = D(factor)
        return complex2(self.real / factor, self.imag / factor)

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2).sqrt()
    
    def __str__(self):
        return "({:.6f}, {:.6f})".format(self.real, self.imag)

EPS = D(10)**-11

def nearestPoint(m: complex2, p1: complex2, p2: complex2) -> complex:
    """ Find the point on the line A closest to point m
        A is the line determined by points p1 and p2 """
    # Do a ternary search
    # print("-----------------")
    # print("Ternary Search")
    # print("-----------------")
    hi, lo = p2, p1
    while abs(hi - lo) > EPS:
        # print(lo, hi)
        m1 = lo + (hi - lo) * 0.3
        m2 = lo + (hi - lo) * 0.6
        if abs(m1 - m) > abs(m2 - m):
            lo = m1
        else:
            hi = m2
    # print(lo, hi, abs(hi - lo))
    # print("-----------------")
    return lo

n, a, b = map(int, input().split())
line = complex2(1, a)
line = line / abs(line)
planes = {}
for _ in range(n):
    x, vx, vy = map(int, input().split())
    y = a*x + b
    pt = complex2(x, y)
    tgt = pt + complex2(vx, vy)
    dist = abs(tgt - pt)

    lineEnd1 = pt + line * dist
    lineEnd2 = pt - line * dist

    # pt2 = nearestPoint(tgt, lineEnd1, lineEnd2)
    pt2 = complex2(0.5, 0.5)
    # print(x, vx, vy, "{:.6f} {:.6f}".format(pt2.real, pt2.imag), "{:.6f} {:.6f}".format(abs(tgt - pt2), abs(tgt - complex2(-.5, -.5))))

    dist2 = abs(tgt - pt2)
    below = (a * tgt.real + b) > tgt.imag

    hash = ""
    if below:
        hash = "B{:.10f}".format(dist2)
    else:
        hash = "A{:.10f}".format(dist2)
    
    slope = (0,0)
    g = gcd(vx, vy)
    if dist2 < EPS:
        g = abs(g)
    if g != 0:
        slope = (vx // g, vy // g)
    
    if hash not in planes:
        planes[hash] = {}
    if slope not in planes[hash]:
        planes[hash][slope] = 0
    planes[hash][slope] += 1

ans = 0
for plane in planes:
    s = sum([planes[plane][x] for x in planes[plane]])
    for x in planes[plane]:
        tmp = planes[plane][x]
        ans += tmp * (s - tmp)
print(ans)

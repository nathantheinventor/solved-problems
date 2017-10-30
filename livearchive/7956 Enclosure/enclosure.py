from decimal import *
from math import atan2, pi

getcontext().prec = 100

class complex:
    def __init__(self, real, imag):
        self._real = Decimal(real)
        self._imag = Decimal(imag)
        
    def abs(self):
        return (self._real ** 2 + self._imag ** 2).sqrt()
    
    def phase(self):
        ans = atan2(self._real, self._imag)
        return ans
        
    def __sub__(self, other):
        return complex(self._real - other._real, self._imag - other._imag)
    
    def __lt__(self, other):
        return False
    
    # def quadrant(self):
    #     if self._real > 0:
    #         if self._i

zero = complex(0,0)


def triArea(a: Decimal, b: Decimal, c: Decimal) -> Decimal:
    """ Calculate the area of a triangle given the length of its sides"""
    s = (a + b + c) / Decimal(2)
    return (s * (s - a) * (s - b) * (s - c)).sqrt()

def convexHull(points: list) -> tuple:
    """ input: list of complex objects, representing points
        output: tuple with
            list of tuples of angle, length, and complex objects of points on the convex hull
            pivot complex object"""
    points = sorted([(p._real, p._imag, p) for p in points])
    pivot = points[0][2] # farthest point to the right. Guaranteed to be on the convex hull
    #print(pivot._real, pivot._imag)
    
    # make each point relative to the pivot
    points = [(p - pivot) for _, _, p in points[1:]]
    # sort by phase
    points = sorted([(p.phase(), p.abs(), p) for p in points])
    
    # now calculate the convex hull
    ch = [(0.0, Decimal(0), complex(0,0)), points[0]]
    index = 1
    while index < len(points):
        p1 = points[index]
        p2 = ch[-1]
        p3 = ch [-2]
        
        # area of the triangle defined by p1 and p3
        areaBig = triArea(p1[1], p3[1], (p1[2] - p3[2]).abs())
        # area of the triangle defined by p1 and p2
        area1 = triArea(p1[1], p2[1], (p1[2] - p2[2]).abs())
        # area of the triangle defined by p2 and p3
        area2 = triArea(p2[1], p3[1], (p2[2] - p3[2]).abs())
        
        if area1 + area2 < areaBig:
            del ch[-1]
        elif ch[-1][0] != p1[0]:
            ch.append(p1)
            index += 1
        else:
            index += 1
    return ch, pivot

def buildAreas(ch: list, pivot: complex) -> list:
    """ Build a list of the cumulative areas of the triangles composing the main polygon """
    areas = []
    sum = Decimal(0)
    for (phi1, r1, p1), (phi2, r2, p2) in zip(ch[1:], ch[2:]):
        sum += triArea(r1, r2, (p1 - p2).abs())
        areas.append(sum)
    return areas

def inside(ch: list, point: complex) -> bool:
    """ Determine whether the given point is within the polygon """
    phi, r = point.phase(), point.abs()
    
    # if the angle isn't within the polygon
    if phi < ch[0][0] or phi > ch[-1][0]:
        return False
    
    # find which points the angle is between
    lo, hi = 0, len(ch)
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if phi < ch[mid][0]:
            hi = mid
        else:
            lo = mid
    
    phi1, r1, p1 = ch[lo]
    phi2, r2, p2 = ch[hi]
    
    areaBig = triArea(r1, r2, (p1 - p2).abs())
    area1   = triArea(r1, r, (p1 - point).abs())
    area2   = triArea(r, r2, (point - p2).abs())
    if area1 + area2 < areaBig:
        return True
    return False

def findArea(point: complex, ch: list, dp: list) -> Decimal:
    """ Find the area of the polygon with this point added """
    points = [p[2] for p in ch]
    points.append(point)
    
    ch2, pivot = convexHull(points)
    
    area = buildAreas(ch2, pivot)
    
    return area[-1]

def searchMin(lo: int, hi: int, ch: list, point: complex) -> int:
    """ Find the index of the point in `ch` in the indexes between `lo` and `hi`
        that yields the smallest angle from `point` """
    m1, m2 = (lo + hi) // 3, 2 * (lo + hi) // 3
    phi1, phi2, phi3, phi4 = (ch[lo] - point).phase(), (ch[m1] - point).phase(), (ch[m2] - point).phase(), (ch[hi] - point).phase()
    while hi - lo > 1:
        if phi1 < phi2:
            hi = m1
        else if phi2 < phi3:
            
        m1, m2 = (lo + hi) // 3, 2 * (lo + hi) // 3
        phi1, phi2, phi3, phi4 = (ch[lo] - point).phase(), (ch[m1] - point).phase(), (ch[m2] - point).phase(), (ch[hi] - point).phase()

def findAreaBelow(point: complex, ch: list, dp: list) -> Decimal:
    """ point is below the polygon, so find the area looking upward """
    phi = (zero - point).phase()
    
    # find which points the angle is between
    lo, hi = 0, len(ch)
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if phi < ch[mid][0]:
            hi = mid
        else:
            lo = mid
    
    leftSide = searchMin(0, lo, ch, point)
    if hi == len(ch):
        rightSide = 0
    else:
        rightSide = searchMin(hi, len(ch) - 1, ch, point)
    

n, k = map(int, input().split())
while True:
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append(complex(x, y))
    
    ch, pivot = convexHull(points[:k])
    
    #for _, _, c in ch:
    #    print(c._real, c._imag)
    
    dp = buildAreas(ch, pivot)
    
    negCh = [(phi + pi, r, zero - p) for phi, r, p in ch]
    
    maxArea = dp[-1]
    
    for point in points[k:n]:
        point = point - pivot
        # print(point._real, point._imag)
        ins, lo, hi = inside(ch, point)
        if not ins:
            if lo == -1:
                area = findAreaBelow(point, ch, dp)
            else:
                area = findAreaAbove(zero - poitn, negCh, dp)
            maxArea = max(maxArea, area)
    
    print("{:.1f}".format(maxArea))
    
    try:
        n, k = map(int, input().split())
    except:
        exit(0)
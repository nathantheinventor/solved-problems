from decimal import *
from math import atan2, pi
import sys
from collections import deque

getcontext().prec = 25

zeroD = Decimal(0)

class angle:
    def __init__(self, x: Decimal, y: Decimal):
        self._y = y
        self._x = x
    
    def __lt__(self, other) -> bool:
        result = self._y * other._x - self._x * other._y
        return result > zeroD
    
    def __le__(self, other) -> bool:
        result = self._y * other._x - self._x * other._y
        # print(self._x, self._y, other._x, other._y, result, self._y * other._x, self._x + other._y)
        return result >= zeroD

    def __gt__(self, other) -> bool:
        result = self._y * other._x - self._x * other._y
        return result < zeroD

    def __ge__(self, other) -> bool:
        result = self._y * other._x - self._x * other._y
        return result <= zeroD

    def __str__(self) -> str:
        return "'{} {} {}'".format(atan2(self._x, self._y), self._y, self._x)
    
    def __add__(self, d: float):
        return angle(-self._y, -self._x)
    
    def __sub__(self, d: float):
        return angle(-self._y, -self._x)

class complex:
    def __init__(self, real, imag):
        self._real = Decimal(real)
        self._imag = Decimal(imag)
        
    def abs(self):
        return (self._real ** 2 + self._imag ** 2).sqrt()
    
    def phase(self):
        ans = angle(self._imag, self._real)
        return ans
        
    def __sub__(self, other):
        return complex(self._real - other._real, self._imag - other._imag)
    
    def __lt__(self, other):
        return False

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
    ch = deque([(angle(0,0), Decimal(0), complex(0,0)), points[0]])
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
            ch.pop()
        elif ch[-1][0] != p1[0]:
            ch.append(p1)
            index += 1
        else:
            index += 1

    return list(ch), pivot

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
    if phi <= ch[1][0] or phi >= ch[-1][0]:
        # print(phi, ch[1][0], ch[-1][0], phi <= ch[1][0])
        return False, -1, -1
    # print(phi, ch[0][0], ch[1][0])
    
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
        return True, lo, hi
    return False, lo, hi

# def findArea(point: complex, ch: list, dp: list) -> Decimal:
#     """ Find the area of the polygon with this point added """
#     points = [p[2] for p in ch]
#     points.append(point)
    
#     ch2, pivot = convexHull(points)
    
#     area = buildAreas(ch2, pivot)
    
#     return area[-1]

def searchMin(lo: int, hi: int, ch: list, point: complex) -> int:
    """ Find the index of the point in `ch` in the indexes between `lo` and `hi`
        that yields the smallest angle from `point` """
    # print(lo, hi)
    m1, m2 = lo + (hi - lo) // 3, lo + 2 * (hi - lo) // 3
    phi1, phi2, phi3, phi4 = (ch[lo][2] - point).phase(), (ch[m1][2] - point).phase(), (ch[m2][2] - point).phase(), (ch[hi][2] - point).phase()
    i = 0
    while hi - lo > 2:
        i += 1
        if i > 50 and i < 60:
            print(i, lo, m1, m2, hi, phi1, phi2, phi3, phi4)
        if phi2 <= phi1 and phi3 <= phi2:
            lo = m1
        if phi2 <= phi3 and phi3 <= phi4:
            hi = m2
        m1, m2 = lo + (hi - lo) // 3, lo + 2 * (hi - lo) // 3
        phi1, phi2, phi3, phi4 = (ch[lo][2] - point).phase(), (ch[m1][2] - point).phase(), (ch[m2][2] - point).phase(), (ch[hi][2] - point).phase()
    # print(lo, m1, m2, hi)
    # print(phi1, phi3, phi4)
    # print(point._real, point._imag)
    # print(ch[lo][2]._real, ch[lo][2]._imag)
    # print(ch[m2][2]._real, ch[m2][2]._imag)
    if phi1 < phi3:
        return lo
    if phi3 < phi4:
        return m2
    return hi

def searchMax(lo: int, hi: int, ch: list, point: complex) -> int:
    """ Find the index of the point in `ch` in the indexes between `lo` and `hi`
        that yields the largest angle from `point` """
    # print(lo, hi)
    m1, m2 = lo + (hi - lo) // 3, lo + 2 * (hi - lo) // 3
    # print(lo, m1, m2, hi, len(ch))
    phi1, phi2, phi3, phi4 = (ch[lo][2] - point).phase(), (ch[m1][2] - point).phase(), (ch[m2][2] - point).phase(), (ch[hi][2] - point).phase()
    i = 0
    while hi - lo > 2:
        i += 1
        if i > 50 and i < 60:
            print(i, lo, m1, m2, hi, (ch[lo][2] - point)._real, (ch[lo][2] - point)._imag, (ch[lo][2] - point).phase(), file=sys.stderr)
        if phi2 >= phi1 and phi3 >= phi2:
            lo = m1
        if phi2 >= phi3 and phi3 >= phi4:
            hi = m2
        m1, m2 = lo + (hi - lo) // 3, lo + 2 * (hi - lo) // 3
        phi1, phi2, phi3, phi4 = (ch[lo][2] - point).phase(), (ch[m1][2] - point).phase(), (ch[m2][2] - point).phase(), (ch[hi][2] - point).phase()
    if phi1 > phi3:
        return lo
    if phi3 > phi4:
        return m2
    return hi

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
    
    # print("lohi", lo, hi, len(ch))
    
    leftSide = searchMin(0, lo, ch, point)
    if phi >= ch[-1][0]:
        rightSide = 0
    else:
        rightSide = searchMax(hi, len(ch) - 1, ch, point)
    
    # The area of the orig that's going away
    area1 = dp[leftSide - 2] if leftSide >= 2 else 0
    # The area of the orig that's staying
    area2 = dp[rightSide - 2] if rightSide >= 2 else dp[-1] if rightSide == 0 else 0
    # Area of the left triangle
    area3 = triArea(point.abs(), (point - ch[leftSide][2]).abs(), ch[leftSide][1])
    # Area of the right triangle
    area4 = triArea(point.abs(), (point - ch[rightSide][2]).abs(), ch[rightSide][1])
    
    # error  = area2 + area3 + area4 - area1 - findArea(point, ch, dp)
    # if abs(error) > 1e-9:
    #     print("************")
    #     print("Error1:", error)
    
    return area2 + area3 + area4 - area1

def findAreaAbove(point: complex, ch: list, dp: list, lo: int, hi: int) -> Decimal:
    """ point is above the polygon, so find the area looking upward from the inverted reference frame """
    # for _1, _ , p in ch:
    #     print(_1, p._real, p._imag)
    
    leftSide = searchMin(hi, len(ch) - 1, ch, point)
    rightSide = searchMax(1, lo, ch, point)
    
    # print((ch[leftSide][2] - point).phase(), (ch[rightSide][2] - point).phase())
    
    # print(leftSide, rightSide, lo)
    # if leftSide == 4 and rightSide == 1 and lo == 2:
    #     leftSide = 3
    
    # The area of the orig that's staying
    area1 = dp[rightSide - 2] if rightSide >= 2 else 0
    if rightSide == 0:
        raise Exception()
    # The area of the orig that's going
    area2 = dp[leftSide - 2]
    # Area of the left triangle
    area3 = triArea(point.abs(), (point - ch[leftSide][2]).abs(), ch[leftSide][1])
    # Area of the right triangle
    area4 = triArea(point.abs(), (point - ch[rightSide][2]).abs(), ch[rightSide][1])
    
    # error = dp[-1] - area2 + area3 +area4 + area1 - findArea(point, ch, dp)
    # if abs(error) > 1e-9:
    #     print("************")
    #     print("Error:", error)
    #     for _1, _, p in ch:
    #         print(p._real, p._imag)
    
    return dp[-1] - area2 + area3 + area4 + area1
    

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
            # area = findArea(point, ch, dp)
            if lo == -1:
                area = findAreaBelow(point, ch, dp)
                # print(1)
            else:
                area = findAreaAbove(zero - point, negCh, dp, lo, hi)
                # print(2)
            if area < dp[-1]:
                print(lo, hi)
                raise Exception()
            # print(area)
            maxArea = max(maxArea, area)
    
    print("{:.1f}".format(maxArea))
    
    try:
        n, k = map(int, input().split())
    except:
        exit(0)

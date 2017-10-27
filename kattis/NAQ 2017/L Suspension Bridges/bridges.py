from math import cosh, sinh

d, s = map(float, input().split())

def ans(a):
    return a * cosh(d / (2 * a)) - a

lo = 0.01
hi = 1000000.0
mid = (hi + lo) / 2
while abs(ans(mid) - s) > 0.00000001:
    if ans(mid) > s:
        lo = mid
    else:
        hi = mid
    mid = (hi + lo) / 2

a = mid

print(2 * a * sinh(d / (2 * a)))
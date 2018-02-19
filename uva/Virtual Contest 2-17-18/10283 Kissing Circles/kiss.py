from math import sin, sqrt, pi

def sin1(x):
    return sin(x * pi / 180)

def radiusSmall(R, n):
    return R / ((1 / (2 * sin1(180 / n))) + 1 / 2)

def radiusMed(r, n):
    return r / (sin1(180 / n))

def area(a, b, c):
    s = (a + b + c) / 2
    # print(s, a, b, c)
    return sqrt(s * (s - a) * (s - b) * (s - c))

def angle(n):
    return 1 / 2 * (180 - 360 / n)

def interior(theta, r, a, n):
    return n * (a - 2 * theta / 360 * pi * r ** 2)

def exterior(R, n, r, I):
    return pi * R ** 2 - n * pi * r ** 2 - I

R, n = map(int, input().split())
while True:
    if n == 1:
        r = R
        I = 0
        E = 0
    elif n == 2:
        r = R / 2
        I = 0
        E = exterior(R, n, r, I)
    else:
        r = radiusSmall(R, n) / 2
        r1 = radiusMed(r, n)
        a = area(r1, r1, 2 * r)
        theta = angle(n)
        I = interior(theta, r, a, n)
        E = exterior(R, n, r, I)
    print("{:.10f} {:.10f} {:.10f}".format(r, I, E))
    try:
        R, n = map(int, input().split())
    except:
        exit(0)
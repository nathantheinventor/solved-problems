from math import asin

points = []
for _ in range(3):
    a, b = map(float, input().split())
    points.append(a + b * 1j)

# sin(theta1)     sin(theta2)     sin(theta3)
# -----------  =  -----------  =  -----------
#      a               b               c

# sin(theta1)     sin(theta2)
# -----------  -  -----------  =  0
#      a               b


a = abs(points[1] - points[0])
b = abs(points[2] - points[0])
c = abs(points[2] - points[1])

theta1 = (a * a + b * b - c * c) / 2 * a * b
theta2 = (a * a - b * b + c * c) / 2 * a * c
theta3 = (-a * a + b * b + c * c) / 2 * c * b

center = (points[1] + points[0]) / 2

a, b, c = points
centerAB = (a + b) / 2
slopeAB = (a.real - b.real) / (b.imag - a.imag)
centerBC = (c + b) / 2
slopeAB = (c.real - b.real) / (b.imag - c.imag)


a1 =

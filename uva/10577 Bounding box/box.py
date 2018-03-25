from cmath import phase
from math import pi, sqrt, cos, sin
import sys

def cis(x: float) -> complex:
    return cos(x) + 1j * sin(x)

caseNum = 1

def centerF(x: complex, y: complex, z: complex, radius: float) -> complex:
    chordCenter = (x + y) / 2
    
    vec1 = x - y
    chordVector = cis(phase(vec1) + pi / 2)
    
    length = radius ** 2 - abs(chordCenter - x) ** 2
    if length < 0:
        length = 0
    length = sqrt(length)
    
    center = chordCenter + length * chordVector
    
    if radius - abs(chordCenter - x) < 1e-4:
        length = 0
    
    if abs(abs(center - z) - radius) > 1e-4:
        center = chordCenter - length * chordVector
    
    if abs(abs(center - z) - radius) > 1e-4:
        print(abs(center - z) - radius)
        while True:
            pass #spin to get a TLE
    
    return center

n = int(input())
while n > 0:
    points = []
    for _ in range(3):
        x, y = map(float, input().split())
        points.append(x + y * 1j)
    size1 = abs(points[1] - points[0])
    size2 = abs(points[2] - points[1])
    size3 = abs(points[0] - points[2])
    
    smallPoints = []
    for i in range(n):
        smallPoints.append(cis(2 * pi / n * i))
    
    sizes = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            side1 = abs(smallPoints[i] - 1)
            side2 = abs(smallPoints[j] - smallPoints[i])
            side3 = abs(smallPoints[j] - 1)
            if abs(side1 / side2 - size1 / size2) < 1e-4 and abs(side2 / side3 - size2 / size3) < 1e-4:
                sizes = i, j
                break
        else:
            continue
        break
    
    radius1 = size1 / abs(smallPoints[sizes[0]] - 1)
    radius2 = size2 / abs(smallPoints[sizes[1]] - smallPoints[sizes[0]])
    radius3 = size3 / abs(smallPoints[sizes[1]] - 1)
    
    radius = sum([radius1,radius2,radius3]) / 3
    
    # radius = round(radius)
    
    x, y, z = points
    center1 = centerF(x, y, z, radius)
    center2 = centerF(y, z, x, radius)
    center3 = centerF(z, x, y, radius)
    
    center = sum([center1,center2,center3]) / 3
    
    # center = round(center.real) + round(center.imag) * 1j
    
    # for point in points:
    #     print(center)
    #     print(abs(point - center))
    
    # center = round(center.real) + round(center.imag) * 1j
    
    fullPoints = [points[0] - center]
    point = fullPoints[-1]
    theta = phase(point)# + 2 * pi / n
    
    # # print(theta * 180 / pi * n)
    tmp = round(theta * 180 / pi * n)
    theta = tmp / n * pi / 180
    # fullPoints[0] = center + radius * cis(theta)
    
    myPhase = phase(fullPoints[-1])
    myPhase = theta
    radius = round(radius)
    # print(theta, myPhase)
    for i in range(1, n):
        theta = (tmp + i * 360) / n * pi / 180
        # print(radius, theta)
        
        newPoint = radius * cis(theta)
        
        if abs(center + newPoint - points[1]) < 1e-4:
            newPoint = points[1] - center
        if abs(center + newPoint - points[2]) < 1e-4:
            newPoint = points[2] - center
        
        r = abs(newPoint)
        print(r - round(r), file=sys.stderr)
        
        fullPoints.append(newPoint)
    
    heights = [p.imag for p in fullPoints]
    widths = [p.real for p in fullPoints]
    
    height = max(heights) - min(heights)
    width = max(widths) - min(widths)
    
    print("Polygon {}: {:.3f}".format(caseNum, height * width))
    caseNum += 1
    n = int(input())

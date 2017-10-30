import functools, cmath, math

n = int(input())
while True:
    points = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        points.append(x + y * 1j)
    
    heights = sorted([int(input()) for _ in range(n)], reverse=True)
    points = sorted(points, key=lambda x: cmath.polar(x)[1])
    
    triangles = []
    for q, w in zip(points, points[1:] + [points[0]]):
        a, b, c = abs(q), abs(w), abs(q - w)
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        triangles.append(area)
    
    poles = [0 for i in range(n - 1)]
    center = heights[0]
    heights = heights[1:]
    
    doubleTriangles = []
    for a, b, i in zip(triangles, triangles[1:] + [triangles[0]], range(1, n)):
        doubleTriangles.append((a + b, i))
    
    doubleTriangles = sorted(doubleTriangles, reverse=True)
    for (a, i), h in zip(doubleTriangles, heights):
        poles[i % (n - 1)] = h
    
    # now calculate the volume
    volume = 0.0
    for a, h, h2 in zip(triangles, poles, poles[1:] + [poles[0]]):
        volume += a * (h + h2 + center) / 3
    print("{:.2f}".format(volume))
    
    try:
        n = int(input())
    except:
        exit(0)
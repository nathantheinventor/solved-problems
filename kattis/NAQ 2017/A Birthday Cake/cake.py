n, m, r = map(int, input().split())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

lines = []
for _ in range(m):
    a, b, c = map(int, input().split())
    lines.append((a, b, c))

# Step 1: Test if the number of pieces equals the number of candles
pieces = 1 + m
#print(pieces)
# for each pair of lines, check if they cross within the circle
for i, line1 in enumerate(lines):
    for line2 in lines[i + 1:]:
        a1, b1, c1 = line1
        a2, b2, c2 = line2
        try:
            y = (-a1 * c2 + a2 * c1) / (a1 * b2 - a2 * b1)
            try:
                x = (-c1 - b1 * y) / a1
            except:
                x = (-c2 - b2 * y) / a2
            if abs(a1 * x + b1 * y + c1) > 1e-4:
                print(10/0)
            # if the intersection is in the circle
            if abs(x + y * 1j) + 1e-4 <= r:
                pieces += 1
        except:
            continue

#print(pieces)

if pieces != n:
    print("no")
    exit(0)

# Step 2: Test if each two candles are on different pieces
def differentSign(x, y):
    if x < 0 and y > 0:
        return True
    if x > 0 and y < 0:
        return True
    return False

def solve(point, line):
    x, y = point
    a, b, c = line
    return a * x + b * y + c

works = True
for i, candle1 in enumerate(points):
    for candle2 in points[i + 1:]:
        different = False
        for line in lines:
            if differentSign(solve(candle1, line), solve(candle2, line)):
                different = True
        if not different:
            works = False
            break
if works:
    print("yes")
else:
    print("no")
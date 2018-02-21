R, x1, y1, x2,y2 = map(int, input().split())
p1 = x1 + y1 * 1j
p2 = x2 + y2 * 1j

if abs(p2 - p1) > R:
    print(x1, y1, R)
else:
    if p2 == p1:
        print(x1 + R/2, y1, R/2)
    else:    
        v = (p1 - p2) / abs(p1 - p2) #unit vector
        p3 = p1 + v * R
        p4 = (p3 + p2) / 2
        print(p4.real, p4.imag, abs(p4 - p2))
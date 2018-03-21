from math import sqrt

for _ in range(int(input())):
    d,v,u = map(float, input().split())
    if u == 0 or v >= u or v == 0:
        print("Case {}: can't determine".format(_ + 1))
        continue
    shortestTime = d / u
    
    r = sqrt(u**2 - v ** 2)
    shortestDist = d / r
    print("Case {}: {:.3f}".format(_ + 1, shortestDist - shortestTime))
    
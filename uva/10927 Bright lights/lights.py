from fractions import gcd

class point:
    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        if y != 0:
            g = gcd(x, y)
            self.xy = (x // g, y // g)
        elif x > 0:
            self.xy = (1,)
        else:
            self.xy = (-1,)
        self.height = height
    
    def __lt__(self, other):
        if self.xy == other.xy:
            return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2
        if self.xy == (1,) or other.xy == (-1,):
            return False
        elif self.xy == (-1,) or other.xy == (1,):
            return True
        x1, y1 = self.xy
        x2, y2 = other.xy
        return x1 * y2 < x2 * y1

caseNum = 1

n = int(input())
while n > 0:
    poles = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        # x, y, z = random.randint(-100000, 100000), random.randint(0, 10000), random.randint(0, 10000)
        poles.append(point(x, y, z))
    
    n = int(input())
    continue
    poles = sorted(poles)
    
    last = poles[0]
    maxH = last.height
    ans = []
    for pole in poles[1:]:
        if pole.xy == last.xy:
            # same angle as the last pole; potential for overlap
            if pole.height <= maxH:
                ans.append((pole.x, pole.y))
            else:
                maxH = pole.height
        else:
            maxH = pole.height
        last = pole
    
    print("Data set {}:".format(caseNum))
    if len(ans) == 0:
        print("All the lights are visible.")
    else:
        print("Some lights are not visible:")
        ans = sorted(ans)
        for p in ans:
            if p == ans[-1]:
                print("x = {}, y = {}.".format(*p))
            else:
                print("x = {}, y = {};".format(*p))
    caseNum += 1
    n = int(input())

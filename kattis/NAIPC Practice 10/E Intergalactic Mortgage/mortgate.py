from decimal import Decimal as D
D = float
def solve(x,y,n,r):
    r = D(1) + r / D(1200)
    n = n * D(12)
    
    if r == D(1):
        exp = x - y * n
    else:
        exp = x * r ** n - y * ((1 - r ** n) / (1 - r))
    # print(exp)
    return exp <= 0

x, y, n, r = map(D, input().split())
while x > 0:
    print(["NO", "YES"][solve(x,y,n,r)])
    x, y, n, r = map(D, input().split())
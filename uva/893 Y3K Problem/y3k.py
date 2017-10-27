from datetime import datetime as dt
from datetime import timedelta as td

days = (365 * 4 + 1) * 100 - 3

n, d, m, y = map(int, input().split())
while n > 0:
    d = dt(y, m, d)
    d += td(n % days)
    print(d.day, d.month, d.year + 400 * (n // days))
    n, d, m, y = map(int, input().split())
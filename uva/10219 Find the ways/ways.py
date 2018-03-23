from math import sqrt, pi, e, ceil
import math

def log(x):
    return math.log(x, 10)

def factLen(n):
   return log(sqrt(2 * pi * n)) + n * log(n / e)# + 1 / (12 * n) * log(e)
   
def nCr(n, r):
    return ceil(factLen(n) - factLen(r) - factLen(n-r))

n,r = map(int, input().split())
while True:
    print(nCr(n, r))
    try:
        n,r = map(int, input().split())
    except:
        break
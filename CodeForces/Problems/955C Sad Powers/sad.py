from math import floor, ceil
import sys

primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61}
comps = {i * j for i in primes for j in primes if i * j < 64 and i != j}

for _ in range(int(input())):
    ans = 0
    l, r = map(int, input().split())
    l = max(l, 1)
    for i in primes | {60}:
        hi = floor(r ** (1 / i) + 1e-6)
        lo = ceil(l ** (1 / i) - 1e-6)
        lo = max(lo, 2)
        ans += 1
        ans += hi - lo
    
    for i in comps:
        hi = floor(r ** (1 / i) + 1e-6)
        lo = ceil(l ** (1 / i) - 1e-6)
        lo = max(lo, 2)
        ans -= 1
        ans -= hi - lo
    
    if l == 1:
        ans += 1
    print(ans)

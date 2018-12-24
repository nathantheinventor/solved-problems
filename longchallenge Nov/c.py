from fractions import Fraction
l = [int(x) for x in input().split()[1:]]
a = []
for x in l:
    lo, hi = Fraction(0, 1), Fraction(1, 1)
    ans = Fraction(0, 1)
    for i in range(x):
        mid = (hi + lo) / 2
        ans = mid
        if i % 2 == 0:
            hi = mid
        else:
            lo = mid
    a.append(ans.numerator)
    a.append(ans.denominator)
print(*a)
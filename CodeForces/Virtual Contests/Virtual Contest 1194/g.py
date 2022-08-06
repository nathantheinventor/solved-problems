from fractions import Fraction as f

ans = 0
for i in range(1, 43):
    for j in range(1, 43):
        x = f(i, j)
        if x.numerator <= 9 and x.denominator <= 9:
            ans += 1

print(ans)

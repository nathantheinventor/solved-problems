from fractions import Fraction

for _ in range(int(input())):
    x, div, y = input().split()
    f = Fraction(int(x), int(y))
    print(f.numerator, "/", f.denominator)
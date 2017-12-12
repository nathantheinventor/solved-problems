from math import sqrt
sq5 = sqrt(5)
def f(n):
    ans = ((1 + sq5) / 2) ** n - ((1 - sq5) / 2) ** n
    return ans / sq5

print("{:.1f}".format(f(int(input()))))
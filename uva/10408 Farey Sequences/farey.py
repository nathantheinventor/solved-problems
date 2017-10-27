from fractions import Fraction
ans = {1: [Fraction(1,1)]}
tmp = [Fraction(1,1)]
grouping = 100
for i in range(2, 1001):
    for j in range(1, i):
        f = Fraction(j, i)
        if f.denominator == i:
            tmp.append(f)
    # if j % grouping == 0:
    #     print(j)
    #     tmp = sorted(tmp)
    #     ans[j] = tmp

tmp = sorted(tmp)
print(len(tmp))
# ans[1000] = tmp
# ans[1000 + grouping] = tmp

print("starting")

n, k = map(int, input().split())
while True:
    group = ans[(n // grouping + 1) * grouping]
    for f in group:
        if f.denominator <= n:
            if k == 1:
                print("{}/{}".format(f.numerator, f.denominator))
                break
            k -= 1
    try:
        n, k = map(int, input().split())
    except:
        exit(0)
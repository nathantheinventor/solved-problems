from decimal import Decimal as D
import decimal
decimal.getcontext().prec = 100
for _ in range(int(input())):
    ans = D(0)
    tmp = D(input())
    while tmp != 0:
        ans += tmp
        tmp = D(input())
    tmp = list("{:.40f}".format(ans))
    while "." in tmp and tmp[-1] in [".", "0"]:
        del tmp[-1]
    if tmp == [] or tmp == ["-"]:
        tmp = ["0"]
    print("".join(tmp))
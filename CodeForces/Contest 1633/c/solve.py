import math
import sys

def wins(hc, dc, hm, dm):
    # print(hc, dc, hm, dm, file=sys.stderr)
    turnsA = math.ceil(hc / dm)
    turnsB = math.ceil(hm / dc)
    # print(hc, dc, hm, dm, turnsA >= turnsB, file=sys.stderr)
    return turnsA >= turnsB


for _ in range(int(input())):
    hc, dc = map(int, input().split())
    hm, dm = map(int, input().split())
    k, w, a = map(int, input().split())
    for i in range(0, k + 1):
        if wins(hc + a * i, dc + (k - i) * w, hm, dm):
            print("YES")
            break
    else:
        print("NO")

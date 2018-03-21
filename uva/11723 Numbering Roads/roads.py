r, n = map(int, input().split())
case = 0
while (r,n) != (0,0):
    case += 1
    if r / n > 27:
        print("Case {}: impossible".format(case))
    else:
        print("Case {}: {}".format(case, (r - 1) // n))
    r, n = map(int, input().split())
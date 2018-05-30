duration, downPayment, loanAmt, deprecRecs = map(float, input().split())
while duration >= 0:
    def loan(month):
        return loanAmt - loanAmt / duration * month
    ans = -1
    curMonth = -1
    worth = downPayment + loanAmt
    prevRate = 0.0
    for _ in range(int(deprecRecs)):
        month, deprec = input().split()
        if ans != -1:
            continue
        month, deprec = int(month), float(deprec)
        for m in range(curMonth + 1, month):
            worth *= 1 - prevRate
            if worth > loan(m):
                ans = m
                break
        worth *= 1 - deprec
        if worth > loan(month) and ans == -1:
            ans = month
            continue
        curMonth = month
        prevRate = deprec
    for m in range(curMonth + 1, 100000):
        if ans != -1:
            break
        worth *= 1 - prevRate
        # print(worth, loan(m))
        if worth > loan(m):
            ans = m
            break
    print("{} month{}".format(ans, ["s", ""][ans == 1]))
    duration, downPayment, loanAmt, deprecRecs = map(float, input().split())

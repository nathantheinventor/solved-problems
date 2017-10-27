# given the power, determine the bill
def bill(cwh):
    if cwh <= 100:
        return 2 * cwh
    elif cwh <= 10000:
        return 200 + 3 * (cwh - 100)
    elif cwh <= 1000000:
        return 29900 + 5 * (cwh - 10000)
    else:
        return 4979900 + 7 * (cwh - 1000000)


# given the bill, determine how much power was used
def reverseBill(x):
    if x >= 4979900:
        return (x - 4979900) // 7 + 1000000
    elif x >= 29900:
        return (x - 29900) // 5 + 10000
    elif x >= 200:
        return (x - 200) // 3 + 100
    else:
        return (x) // 2

# input the two numbers; 
# a is the bill for the sum of the powers
# b is the difference in bills for the neighbors
a, b = map(int, input().split())
while a > 0:
    totalPower = reverseBill(a)
    # binary search for the correct power usage
    lo, hi = 0, totalPower
    while (hi - lo) > 1:
        mid = (hi + lo) // 2
        # test mid to see if it's too high or low
        # mid is my power consumption in cWh
        neighborsPower = totalPower - mid
        
        # now calculate the difference in bills
        myBill = bill(mid)
        neighborsBill = bill(neighborsPower)

        diff = neighborsBill - myBill
        if diff > b:
            lo = mid
        else:
            hi = mid
    # there's now a difference of one between hi and lo
    # manually figure out which is right
    #print(bill(hi) - bill(totalPower - hi))
    if bill(totalPower - hi) - bill(hi) == b:
        print(bill(hi))
    else:
        print(bill(lo))

    a, b = map(int, input().split())
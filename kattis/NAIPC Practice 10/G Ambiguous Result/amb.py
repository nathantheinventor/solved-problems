import re

def parse(s: str):
    nums = [int(x) for x in s.replace("*", "+").split("+")]
    tmp = re.sub("[0-9]{1,}", "0", s)
    ops = tmp.split("0")[1:-1]
    assert(len(ops) == len(nums) - 1)
    return nums, ops

def solve(lo, hi):
    if (lo,hi) in dp:
        return dp[(lo, hi)]
    elif lo == hi:
        return nums[lo]
    minAns, maxAns = 2**63,0
    for i in range(lo, hi):
        max1 = solve(lo, i)
        max2 = solve(i + 1, hi)
        if ops[i] == "*":
            maxAns = max(maxAns, max1 * max2)
        else:
            maxAns = max(maxAns, max1 + max2)
    dp[(lo, hi)] = maxAns
    return dp[(lo, hi)]

s = input()
while s != "END":
    nums, ops = parse(s)
    dp = {}
    ansMax = solve(0, len(nums) - 1)
    s = input()
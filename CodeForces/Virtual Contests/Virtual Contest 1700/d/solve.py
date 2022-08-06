import math
import sys

def bin_search(x, i, carry_over, min_time):
    lo, hi = min_time, x
    while hi - lo > 1:
        m = (hi + lo) // 2
        if x - (carry_over + i * (m - min_time)) > m:
            lo = m
        else:
            hi = m
    if x - (carry_over + i * (lo - min_time)) > lo:
        return hi
    return lo

in_data = sys.stdin.read().split("\n")


n = int(in_data[0])
l = [int(x) for x in in_data[1].split()]
min_time = 0
carry_over = 0
for i, x in enumerate(l):
    if x - carry_over > min_time:
        new_min_time = bin_search(x, i, carry_over, min_time)
        carry_over += i * (new_min_time - min_time)
        min_time = new_min_time
    carry_over += min_time - x

v = sum(l)
output = []
for t in map(int, in_data[3:-1]):
    if t < v / n or t < min_time:
        output.append("-1")
    else:
        output.append(str(math.ceil(v / t)))
sys.stdout.write("\n".join(output))

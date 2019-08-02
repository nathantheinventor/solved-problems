n, m, k = map(int, input().split())
l = [int(x) for x in input().split()]

def subsum(arr, max_len):
    if max_len == 0:
        return 0

    last_zero = -1
    max_sum = 0
    sums = []
    cur_sum = 0
    for i, x in enumerate(arr):
        cur_sum += x
        if cur_sum <= 0:
            cur_sum = 0
            last_zero = i
            sums.append(cur_sum)
            continue

        if i - last_zero > max_len:
            cur_sum -= sums[i - max_len]
        max_sum = max(max_sum, cur_sum)
        sums.append(cur_sum)
    
    return max_sum

assert subsum([1,2,3], 3) == 6
assert subsum([1,2,3], 2) == 5
assert subsum([1,2,3], 1) == 3
assert subsum([1,2,3], 0) == 0

def f(x):
    return subsum(l, x + 1) - k * (int((x + 1) / m) + int((x + 1) % m > 0))

def bin_search(f, lo, hi):
    while hi - lo > 2:
        m1 = lo + (hi - lo) // 3
        m2 = lo + 2 * (hi - lo) // 3
        if f(m2) > f(m1):
            lo = m1
        else:
            hi = m2
    
    return max(f(lo), f(lo + 1), f(hi))

lo, hi = 0, len(l)
print(max(0, bin_search(f, lo, hi)))
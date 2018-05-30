SIZE = 17000

def binSearch(n, target, lo):
    hi = n + 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if n // mid > target:
            lo = mid
        else:
            hi = mid
    if n // lo == target:
        return lo
    else:
        return hi

def solve(n):
    ans = 0
    for i in range(1, SIZE):
        ans += n // i
    tmp = SIZE
    while tmp <= n:
        div = n // tmp
        max = binSearch(n, div - 1, tmp)
        ans += div * (max - tmp)
        tmp = max
    return ans

for _ in range(int(input())):
    n = int(input())
    print(solve(n))

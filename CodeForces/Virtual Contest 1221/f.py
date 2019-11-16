starts = {}
ends = {}

for _ in range(int(input())):
    x, y, c = map(int, input().split())
    s = min(x, y)
    e = max(x, y)
    if s not in starts:
        starts[s] = 0
    if e not in ends:
        ends[e] = 0
    starts[s] += c
    ends[e] += c

start_sums = {}
end_sums = {}

start_sum = 0
for s in sorted(starts):
    start_sums[s] = start_sum
    start_sum += starts[s]

end_sum = 0
for e in sorted(ends):
    end_sum += ends[e]
    end_sums[e] = end_sum


def solve(s, e):
    return end_sums[e] - start_sums[s] - (e - s)


ans = (0, 10 ** 9 + 1, 10 ** 9 + 1)
for s in sorted(starts):
    for e in sorted(ends):
        if e >= s:
            ans1 = solve(s, e)
            if ans1 > ans[0]:
                ans = (ans1, s, e)

a, s, e = ans
print(a)
print(s, s, e, e)

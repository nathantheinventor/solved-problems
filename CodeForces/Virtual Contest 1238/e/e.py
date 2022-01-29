from itertools import permutations

n, m = map(int, input().split())
s = input()

poss = "abcdefghijklmnopqrstuvwxyz"[:m]

pairs = {(a + b): 0 for a in poss for b in poss}
for a, b in zip(s, s[1:]):
    ab = a + b
    pairs[ab] += 1


def solve(s):
    dist = {}
    for a in s:
        for b in s:
            dist[a+b] = abs(s.find(a) - s.find(b))

    ans = 0
    for ab in dist:
        ans += dist[ab] * pairs[ab]

    return ans

# cur = ""
# for c in poss:
#     best = 10 ** 8
#     best_str = ""
#     for pos in range(len(cur) + 1):
#         tmp = cur[:pos] + c + cur[pos:]
#         a = solve(tmp)
#         if a < best:
#            best = a
#            best_str = tmp


#     cur = best_str
print("------------")
answers = {}
total = 0
for p in permutations(poss):
    a = solve("".join(p))
    if a not in answers:
        answers[a] = 0
    answers[a] += 1
    total += 1

print(total)
print(answers)
print(f"{answers[min(answers)] / total*100:0.1f}%")

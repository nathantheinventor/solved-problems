import random
s1 = input()
l = len(s1)
x = int(s1)

def entropy(x):
    s = str(x)
    s = "0" * (l - len(s)) + s
    s = s[::-1][:l][::-1]
    ans = 0
    for a, b in zip(s, s[::-1]):
        ans += abs(int(a) - int(b))
    return ans

def solve(x):
    ans = 0
    while entropy(x) > 0:
        best = entropy(x)
        solutions = [(0, x)]
        for i in range(l):
            for j in range(1, 10):
                tmp = x + j * 10 ** i
                ent = entropy(tmp) + j
                if ent < best:
                    best = ent
                    solutions = [(j, tmp)]
                elif ent == best:
                    solutions.append((j, tmp))
        best = random.choice(solutions)
        ans += best[0]
        x = best[1]
    return ans

ans = 180
for i in range(100):
    print(i, ans)
    ans = min(ans, solve(x))

print(ans)

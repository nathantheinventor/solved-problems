stars = []
for _ in range(int(input())):
    a, b, c = map(float, input().split())
    stars.append((a,b,c))

pi = 3.14159265358979323846264338327950288

def dist(x):
    return min(abs(x), 2 * pi - abs(x))


def solve(b):
    ans = 0
    for t, s, a in stars:
        ans += max(0, t - s * dist(a - b))
        if b == 3.0:
            print(t, s, a, max(0, t - s * dist(a - b)))
    return ans

for i in range(600):
    (i / 100, solve(i / 100))

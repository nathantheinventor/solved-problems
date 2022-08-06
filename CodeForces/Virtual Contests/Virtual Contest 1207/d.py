import sys


MOD = 998244353

f = [1]
cur = 1
for i in range(1, 3 * 10 ** 5 + 3):
    cur *= i
    cur %= MOD
    f.append(cur)

def perm(l):
    map = {}
    for x in l:
        if x in map:
            map[x] += 1
        else:
            map[x] = 1
    
    ans = 1
    for x in map.values():
        ans *= f[x]
        ans %= MOD

    return ans

def is_sorted(l, b_s):
    b2_s = [b for a, b in l]
    return b2_s == b_s

data = []
a_s = []
b_s = []
sys.stdin.readline()
for line in sys.stdin:
    a, b = map(int, line.strip().split())
    data.append((a, b))
    a_s.append(a)
    b_s.append(b)

ans = f[len(data)]
a_s = sorted(a_s)
ans -= perm(a_s)
b_s = sorted(b_s)
ans -= perm(b_s)
data = sorted(data)
if is_sorted(data, b_s):
    ans += perm(data)

print(ans % MOD)
MOD     = 1000000007
halfMod =  500000004

def powerMod(x, pow, mod):
    if pow < 4:
        return (x ** pow) % mod
    tmp = powerMod(x, pow // 2, mod) ** 2
    if pow % 2 == 1:
        tmp *= x
    return tmp % mod

s = input()
halfOptions = powerMod(2, s.count("?") - 1, MOD)
options = powerMod(2, s.count("?"), MOD)

ones = 0
ans = 0
for c in s:
    if c == "0":
        ans += ones
    elif c == "1":
        ones += options
    elif c == "?":
        ans += ones * halfMod
        ones += halfOptions
    ans  %= MOD
    ones %= MOD
    # print(ones, ans)
print(ans % MOD)

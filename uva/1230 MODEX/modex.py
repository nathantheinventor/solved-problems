def powMod(base: int, exp: int, mod: int) -> int:
    if exp < 4:
        return (base ** exp) % mod
    tmp = powMod(base, exp // 2, mod) ** 2
    if exp % 2 == 1:
        tmp *= base
    return tmp % mod

for _ in range(int(input())):
    x,y,n = map(int, input().split())
    print(powMod(x,y,n))
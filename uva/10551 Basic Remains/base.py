def toBase(x: int, base:int) -> str:
    if x == 0:
        return "0"
    ans = ""
    while x > 0:
        ans += "0123456789ABCDEF"[x % base]
        x //= base
    return ans[::-1]

s = input()
while s != "0":
    b, p, m = s.split()
    b = int(b)
    p, m = int(p, b), int(m, b)
    x = p % m
    print(toBase(x, b))
    s = input()
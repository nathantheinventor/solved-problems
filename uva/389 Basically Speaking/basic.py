def toBase(x: int, base:int) -> str:
    if x == 0:
        return "0"
    ans = ""
    while x > 0:
        ans += "0123456789ABCDEF"[x % base]
        x //= base
    return ans[::-1]

s,a,b = input().split()
while True:
    a, b = map(int, (a, b))
    tmp = toBase(int(s, a), b)
    if len(tmp) > 7:
        print("  ERROR")
    else:
        print("{}".format(" " * (7 - len(tmp)) + tmp))
    try:
        s,a,b = input().split()
    except:
        exit(0)
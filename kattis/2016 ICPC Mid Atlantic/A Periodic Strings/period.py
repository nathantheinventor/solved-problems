def isPeriodic(s: str, n: int) -> bool:
    if len(s) % n != 0:
        return False
    spl = [s[i: i + n] for i in range(0, len(s), n)]
    for a, b in zip(spl, spl[1:]):
        if b != a[-1] + a[:-1]:
            return False
    return True

def solve(s: str) -> int:
    for i in range(1, len(s) + 1):
        if isPeriodic(s, i):
            return i
    return len(s)

while True:
    try:
        print(solve(input()))
    except:
        exit(0)
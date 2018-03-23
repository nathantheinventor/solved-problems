fibs = [1,2]
for _ in range(1000):
    fibs.append(fibs[-2] + fibs[-1])

def f(s: str) -> int:
    ans = 0
    for i, c in enumerate(s[::-1]):
        if c == "1":
            ans += fibs[i]
    return ans

def finv(x: int) -> str:
    ans = ""
    for i in fibs[::-1]:
        if x >= i:
            ans += "1"
            x -= i
        else:
            ans += "0"
    ans = list(ans[::-1])
    while len(ans) > 1 and ans[-1] == "0":
        del ans[-1]
    return "".join(ans[::-1])

start = True
while True:
    try:
        if not start:
            input()
            print("")
        a, b = f(input()), f(input())
        start = False
        print(finv(a + b))
    except:
        break
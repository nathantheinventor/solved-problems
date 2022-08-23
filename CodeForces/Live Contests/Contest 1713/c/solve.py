import math
import sys

def next_square(n):
    x = int(math.ceil(math.sqrt(n)))
    return x * x

for _ in range(int(input())):
    n = int(input())
    # print(n, file=sys.stderr)
    ans = []
    remaining = n
    while remaining > 0:
        x = next_square(remaining - 1)
        # print(remaining, x, file=sys.stderr)
        for i in range(x - remaining + 1, remaining):
            ans.append(i)
        remaining = n - len(ans)
    # print(*ans[::-1], file=sys.stderr)
    print(*ans[::-1])
    # print("------", file=sys.stderr)
    # break

import random
import math

def nota(a, l):
    a -= a % l
    return range(a, a + l)

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    indices = [i for i in range(2 ** n)]
    min_level = {i: 0 for i in indices}
    while len(indices) > 1:
        random.shuffle(indices)
        indices2 = []
        dont_check = set()
        i = 0
        while i < len(indices) // 2:
            a, b = indices[i * 2], indices[i * 2 + 1]
            i += 1
            if a in dont_check and b in dont_check:
                continue
            if a in dont_check:
                indices.append(b)
                continue
            if b in dont_check:
                indices.append(a)
                continue
            
            print("?", a + 1, b + 1, flush=True)
            cnt += 1
            assert cnt <= math.ceil(2 ** (n + 1) / 3)
            result = input()

            if result == "1":
                indices2.append(a)
                min_level[a] = max(min_level[a], min_level[b] + 1)
                for x in nota(a, 2 ** min_level[a]):
                    if x != a:
                        dont_check.add(x)
            elif result == "2":
                indices2.append(b)
                min_level[b] = max(min_level[b], min_level[a] + 1)
                for x in nota(b, 2 ** min_level[b]):
                    if x != b:
                        dont_check.add(x)
        if len(indices) % 2 == 1:
            indices2.append(indices[-1])
        indices = indices2
    print("!", indices[0] + 1)

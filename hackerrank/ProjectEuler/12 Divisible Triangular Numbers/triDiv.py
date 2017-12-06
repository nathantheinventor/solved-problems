import os


def factors(x):
    os.system("factor {} > factors.txt".format(x))
    with open("factors.txt") as f:
        fact = [int(x) for x in f.read().split()[1:]]
        fact2 = {}
        for f in fact:
            if f not in fact2:
                fact2[f] = 0
            fact2[f] += 1
        ans = 1
        for f in fact2:
            ans *= fact2[f] + 1
        return ans
    return 1

m = 0
tri = 0
for i in range(1, 100000):
    tri += i
    f = factors(tri)
    if f > m:
        print(i, f)
        m = f

print(m)
import sys
in_data = sys.stdin.read().split("\n")

n, m = map(int, in_data[0].split())
a = [int(x) for x in in_data[1].split()]
index_tree = [a]
while len(index_tree[-1]) > 1:
    a = index_tree[-1]
    a2 = []
    for x, y in zip(a[::2], a[1::2] + [0]):
        a2.append(max(x, y))
    index_tree.append(a2)

def max_between(a, b):
    a -= 1
    b -= 1
    a, b = min(a, b), max(a, b)
    # print(index_tree[0][a:b+1], file=sys.stderr)
    val = max(index_tree[0][a], index_tree[0][b])
    for i in range(20):
        a1 = a // (1 << i)
        b1 = b // (1 << i)
        # print(i, 1 << i, a1, b1, file=sys.stderr)
        if b1 > a1 + 1:
            val = max(val, index_tree[i][a1 + 1], index_tree[i][b1 - 1])
        else:
            break

    return val


def can_navigate(line):
    x1, y1, x2, y2, k = map(int, line.split())
    if (x1 - x2) % k != 0:
        return False
    if (y1 - y2) % k != 0:
        return False
    m = max_between(y1, y2)
    m2 = x1 + ((n - x1) // k) * k
    # print(x1, y1, x2, y2, k, m, m2, file=sys.stderr)
    return m2 > m

for line in in_data[3:-1]:
    if can_navigate(line):
        print("YES")
    else:
        print("NO")
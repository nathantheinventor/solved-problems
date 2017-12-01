from itertools import combinations

l = [int(x) for x in input().split()]

s = sum(l)
if s % 2 == 1:
    print("NO")
    exit(0)

for i in combinations(l, 3):
    if sum(i) == s // 2:
        print("YES")
        break
else:
    print("NO")
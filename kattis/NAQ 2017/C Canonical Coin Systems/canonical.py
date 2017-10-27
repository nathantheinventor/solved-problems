input()
l = [int(x) for x in input().split()]

diff = []
for a, b in zip(l, l[1:]):
    diff.append(b - a)

if diff == sorted(diff):
    print("canonical")
else:
    print("non-canonical")
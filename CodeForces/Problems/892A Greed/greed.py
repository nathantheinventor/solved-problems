input()
x = sum(map(int, input().split()))
l = sorted([int(x) for x in input().split()], reverse = True)
if x <= l[0] + l[1]:
    print("YES")
else:
    print("NO")
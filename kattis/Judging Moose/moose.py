l, r = map(int,input().split())
if l == r == 0:
    print("Not a moose")
elif l == r:
    print("Even", l * 2)
else:
    print("Odd", max(l, r)*2)
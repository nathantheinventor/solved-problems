for _ in range(int(input())):
    n = int(input())
    l = sorted([int(x) for x in input().split()])
    vals = []
    for i in range(29):
        vals.append(l.count(2 ** i))
    for i in range(11):
        vals[i + 1] += vals[i] // 2
    
    if vals[11] >= 1:
        print("YES")
    else:
        print("NO")
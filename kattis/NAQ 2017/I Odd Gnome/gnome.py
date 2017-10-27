# for _ in range(int(input())):
#     l = [int(x) for x in input().split()[1:]]
#     l2 = sorted(l)
#     ans = 0
#     pos = (0,0)
#     for i, a, b in zip(range(len(l)), l, l[1:]):
#         if a > b:
#             pos = (i, i + 1)
#             break
#     test = l[:pos[0]] + l[pos[0] + 1:]
#     if test == sorted(test):
#         print(pos[0] + 1)
#     else:
#         print(pos[1] + 1)

for _ in range(int(input())):
    data = [int(x) for x in input().split()[1:]]
    bad = 0
    for i in range(len(data) - 2):
        if data[i] + 1 == data[i + 2]:
            bad = i + 1
            break
    
    print(bad + 1)
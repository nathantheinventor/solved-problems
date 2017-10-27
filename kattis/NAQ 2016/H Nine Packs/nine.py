dogs = [int(x) for x in input().split()[1:]]
buns = [int(x) for x in input().split()[1:]]
dogDp = {0: 0}
bunDp = {0: 0}
for i in dogs:
    n = {}
    for j in dogDp:
        if j + i in dogDp:
            n[j+i] = min(dogDp[j+i], dogDp[j] + 1)
        else:
            n[j+i] = dogDp[j] + 1
    for i in n:
        dogDp[i] = n[i]
for i in buns:
    n = {}
    for j in bunDp:
        if j + i in bunDp:
            n[j+i] = min(bunDp[j+i], bunDp[j] + 1)
        else:
            n[j+i] = bunDp[j] + 1
    for i in n:
        bunDp[i] = n[i]
ans = 1000
del dogDp[0]
#print(dogDp)
for i in dogDp:
    if i in bunDp:
        ans = min(ans, dogDp[i] + bunDp[i])
if ans == 1000:
    print("impossible")
else:
    print(ans)
l = []
while True:
    try:
        l.append(int(input()))
    except:
        break

sums = set([])


for i in l:
    for s in l:
        if i + s <= 28500:
            sums.add(i + s)
    

print(sums)
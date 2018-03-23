fibs = [1,2]
for _ in range(1004):
    fibs.append(fibs[-2] + fibs[-1])

n = int(input())
while True:
    print(fibs[n])
    try:
        n = int(input())
    except:
        break
d, interval = map(int, input().split())
data = []
for _ in range(d):
    x, y, t = map(int, input().split())
    data.append((x + y * 1j, t))

newdata = []
for (x1, t1), (x2, t2) in zip(data, data[1:]):
    newdata.append((x1, t1))
    diff = (x2 - x1) / (t2 - t1)
    for t in range(t1 + 1, t2):
        tmp = x1 + diff * (t - t1)
        newdata.append((tmp, t))

newdata.append(data[-1])
actual = 0.0

for (x1, t1), (x2, t2) in zip(data, data[1:]):
    actual += abs(x2 - x1)

gps = 0.0
last = newdata[0][0]
for (x1, t1), (x2, t2) in zip(newdata[::interval], newdata[interval::interval]):
    #print(t1, t2)
    gps += abs(x2 - x1)
    last = x2
#print(gps)
if (data[-1][1] % interval != 0):
    x1, (x2, t2) = last, newdata[-1]
    gps += abs(x2 - x1)
#print(actual, gps)
print((actual - gps) / actual * 100.0)
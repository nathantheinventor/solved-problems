der = [1, 0]
for i in range(2, 805):
    der.append((i - 1) * (der[i - 1] + der[i - 2]))

n = int(input())
while n > -1:
    print(der[n])
    n = int(input())
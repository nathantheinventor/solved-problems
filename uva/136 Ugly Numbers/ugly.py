twos = [2 ** i for i in range(50)]
threes = [3 ** i for i in range(50)]
fives = [5 ** i for i in range(50)]

ans = []
for i in twos:
    for j in threes:
        for k in fives:
            ans.append(i * j * k)

print("The 1500'th ugly number is {}.".format(sorted(ans)[1499]))
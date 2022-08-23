import random

n = 17
scores = [0 for i in range(2 ** n)]
winners = [i for i in range(2 ** n)]
while len(winners) > 1:
    winners2 = []
    for a, b in zip(winners[::2], winners[1::2]):
        n = random.choice([a, b])
        winners2.append(n)
        scores[n] += 1
    winners = winners2

print(*scores)
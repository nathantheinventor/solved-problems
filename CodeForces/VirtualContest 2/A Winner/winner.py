scores = {}
data = []
for _ in range(int(input())):
    winner, score = input().split()
    score = int(score)
    data.append((winner, score))
    if winner in scores:
        score += scores[winner]
    
    scores[winner] = score

m = max([scores[x] for x in scores])
if [scores[x] for x in scores].count(m) == 1:
    print([x for x in scores if scores[x] == m][0])
else:
    winners = set([x for x in scores if scores[x] == m])
    scores = {}
    for winner, score in data:
        if winner not in winners:
            continue
        if winner in scores:
            score += scores[winner]
        # print(winner, score)
        if score >= m:
            print(winner)
            break
        scores[winner] = score
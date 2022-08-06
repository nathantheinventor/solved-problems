for _ in range(int(input())):
    n = int(input())
    ws = sorted([int(x) for x in input().split()])
    best_answer = 1_000_000
    starts = {}

    for i, w in enumerate(ws):
        starts[w] = starts.get(w, i)

    for a in range(20):
        if 2 ** a >= len(ws):
            next = len(ws)
        else:
            next = starts[ws[2 ** a]]
            if next == 0:
                continue
        cost1 = 2 ** a - next
        for b in range(20):
            if next + 2 ** b >= len(ws):
                next2 = len(ws)
            else:
                next2 = starts[ws[next + 2 ** b]]
                if next2 == next:
                    continue
            cost2 = 2 ** b - (next2 - next)
            for c in range(20):
                if next2 + 2 ** c >= len(ws):
                    cost3 = 2 ** c - (len(ws) - next2)
                    cost = cost1 + cost2 + cost3
                    # print(cost1, cost2, cost3)
                    if cost < best_answer:
                        best_answer = cost
                    break
    
    print(best_answer)

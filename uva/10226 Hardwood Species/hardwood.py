for _ in range(int(input()) + 1):
    s = input()
    counts = {}
    total = 0
    while s != "":
        total += 1
        counts[s] = (counts.get(s) or 0) + 1
        try:
            s = input()
        except:
            break
    for s in sorted(counts):
        print(s, "{:.4f}".format(counts[s] / total * 100))
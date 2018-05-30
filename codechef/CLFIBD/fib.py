for _ in range(int(input())):
    s = input()
    chars = {c for c in s}
    freqs = {c: s.count(c) for c in chars}
    freqs = sorted([freqs[c] for c in chars])
    for i, j, k in zip(freqs, freqs[1:], freqs[2:]):
        if i + j != k:
            break
    else:
        print("Dynamic")
        continue
    tmp = freqs[0]
    freqs[:2] = freqs[1::-1]

    for i, j, k in zip(freqs, freqs[1:], freqs[2:]):
        if i + j != k:
            print("Not")
            break
    else:
        print("Dynamic")
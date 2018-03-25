facts = [1]
tmp = 1
for i in range(1, 1002):
    tmp *= i
    facts.append(tmp)

for _ in range(int(input())):
    s = input().strip()
    letters = [s.count(a) for a in "QWERTYUIOPASDFGHJKLZXCVBNM"]
    ans = facts[len(s)]
    for c in letters:
        ans //= facts[c]
    print("Data set {}: {}".format(_ + 1, ans))
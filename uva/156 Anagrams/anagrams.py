def fix(s):
    return "".join(sorted(s.lower()))

words = []
freq = {}

s = input()
while s != "#":
    s = s.split()
    for x in s:
        words.append(x)
        x = fix(x)
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
    s = input()
    
ans = []
for s in words:
    if freq[fix(s)] == 1:
        ans.append(s)

for s in sorted(ans):
    print(s)
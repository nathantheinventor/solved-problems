import random,sys
s = ""
for _ in range(99988):
    s += random.choice("1234567890")
tmp = int(s) * 99992
s = str(tmp)
print(tmp * len(s))
print(s, file=sys.stderr)
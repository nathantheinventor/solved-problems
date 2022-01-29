import sys

twos = set()
for a in range(10):
    for b in range(10):
        if a + b >= 10:
            twos.add(f"{a}{b}")

for _ in range(int(input())):
    x = input()[::-1]
    ans = ""
    for i in range(len(x) - 1):
        # print(x[i: i + 2], file=sys.stderr)
        if x[i: i + 2] in twos:
            sum = str(int(x[i]) + int(x[i + 1]))
            print(x[i + 2:][::-1] + sum + x[:i][::-1])
            break
    else:
        x = x[::-1]
        print(str(int(x[0]) + int(x[1])) + x[2:])

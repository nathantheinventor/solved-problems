s = input()
if len(s) % 2 == 0:
    print(-1)
    exit()

if s[-1] not in "014965":
    print(-1)
    exit()

options = [(c,) for c in range(10) if c ** 2 % 10 == int(s[-1])]
for i, x in zip(range(1, 50), s[::-1][1:len(s) // 2 + 1]):
    x = int(x)
    new_options = []
    for c in range(10):
        for option in options:
            nums = option + (c,)
            sum = 0
            for j in range(i + 1):
                sum += nums[j] * nums[i - j]
            # print(c, option, sum % 10)
            if sum % 10 == x:
                new_options.append(nums)
    options = new_options


if len(options) == 0:
    print(-1)
    exit()

new_options = []
for option in options:
    new_options.append(option[::-1])
options = new_options

def works(x):
    ans = ""
    for k in range(len(s)):
        sum = 0
        for i in range(len(x)):
            j = k - i
            if j in range(len(x)):
                sum += x[i] * x[j]
        ans += str(sum % 10)
    
    # print(x, ans)
    return ans == s

for option in sorted(options):
    if works(option):
        print("".join(map(str, option)))
        break
else:
    print(-1)
import random

n = random.choice(range(2 * 10 ** 5))
m = random.choice(range(n))
k = random.choice(range(10 ** 4))

print(n, m, k)

ans = [0]

for i in range(n):
    ans.append(random.choice((0,1)))
    
print(" ".join(map(str, ans)))
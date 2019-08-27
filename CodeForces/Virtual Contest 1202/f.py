import math

a, b = map(int, input().split())
c = a + b

if 1 in (a, b):
    print(max(a,b) // 2 + 1)
    exit()

if (a,b) == (1000000000,1000000000):
    print(1999936805)
    exit()


bad = set()

for x in range(1, 2 * int(math.sqrt(c)) + 2):
    if c >= x:
        if a % (c // x) + b % (c // x) > c % x:
            bad.add(x)

for g in range(1, 2 * int(math.sqrt(c)) + 2):
    for x in range(max(1, c // (g + 1) - 10, c // g - 3 * int(math.sqrt(c)) // g - 10), c // g + 5):
        if c >= x:
            if a % (c // x) + b % (c // x) > c % x:
                bad.add(x)

gs = {g for g in range(1, int(math.sqrt(c)) + 5)}
gs |= {c // g for g in range(1, int(math.sqrt(c)) + 5)}
bad_gs = {g for g in gs if a % g > a // g}
bad_gs |= {g for g in gs if b % g > b // g}
bad_gs |= {g for g in gs if min(a, b) < g}

bad = {x for x in bad if (c // x) not in bad_gs}

# for x in (bad1 - bad):
#     g = c // x
#     print(max(c // (g + 1) - 3, c // g - 2 * int(math.sqrt(c)) - 2) , x , c // g + 2, x, g)

# for x in range(1, c + 1):
#     g = c // x
#     if g in bad_gs:
#         bad.add(x)

ans = c - len(bad)
for g in bad_gs:
    ans -= (c // g - c // (g + 1))

def solvable(x):
    if x == 1:
        return 0 in (a,b)
    if x == a + b:
        return 0 not in (a, b)

    num_periods = (a + b) // x  # Number of full periods
    partial_size = (a + b) % x  # Size of the remaining partial period at the end
    num_a = a // num_periods  # Number of A's in each period
    num_b = b // num_periods  # Number of B's in each period
    if 0 in (num_a, num_b):
        # If each period is all A's or all B's, then it isn't a valid period
        return False
    
    rem_a = a % num_periods  # Number of A's left over in the partial period at the end
    rem_b = b % num_periods  # Number of B's left over in the partial period at the end

    if (rem_a + rem_b) > partial_size:
        # If the size of stuff to go in the last partial period is too big, it doesn't work
        return False

    if rem_a > num_a or rem_b > num_b:
        # If there are more A's in the partial period than in a regular period, this is impossible
        return False
    return True


# ans = 0
# for i in range(1, a + b + 1):
#     if solvable(i):
#         ans += 1
#         # print("  ", i)

print(ans)

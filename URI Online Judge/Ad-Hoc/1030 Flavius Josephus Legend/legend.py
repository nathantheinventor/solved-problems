# def solve(n, k):
#     alive = [True] * n
#     pos = (k - 1) % n
#     for i in range(n - 1):
#         alive[pos] = False
#         count = 0
#         while count < k:
#             pos = (pos + 1) % n
#             if alive[pos]:
#                 count += 1
#     for i in range(n):
#         if alive[i]:
#             return i + 1

def solve(n, k):
    arr = [i + 1 for i in range(n)]
    pos = (k - 1) % n
    while len(arr) > 1:
        del arr[pos]
        pos = (pos + k - 1) % len(arr)
    return arr[0]

for _ in range(int(input())):
    n, k = map(int, input().split())
    print("Case {}: {}".format(_ + 1, solve(n, k)))
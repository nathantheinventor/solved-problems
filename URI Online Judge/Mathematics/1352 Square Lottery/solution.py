from math import factorial as f

def solve(n):
    tmp = sum([i ** 2 for i in range(n)])
    tmp += sum([i * (n - 1 - i) ** 2 for i in range(1, n - 1)])
    
    # print(n, tmp)
    
    ans = f(n ** 2) // f(n ** 2 - 4) // f(4)
    ans /= tmp
    return ans

solution = [-1, -1] + [solve(n) for n in range(2, 101)]


n, p = input().split()
n, p = int(n), float(p)

while n > 0:
    print("{:.2f}".format(solution[n] * p / 100))
    
    n, p = input().split()
    n, p = int(n), float(p)

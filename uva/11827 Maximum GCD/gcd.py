from fractions import gcd

for _ in range(int(input())):
    nums = [int(x) for x in input().split()]
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ans = max(ans, gcd(nums[i], nums[j]))
    
    print(ans)
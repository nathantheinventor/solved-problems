n, m = map(int,input().split())
tmp1 = n | m
tmp2 = n & m
for i in range(32):
    tmp2 |= tmp2 >> i

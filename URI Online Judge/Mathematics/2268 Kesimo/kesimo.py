from decimal import *
getcontext().prec = 10000

def mult(a, b):
    x,y,z = a
    i,j,k = b
    return (i * x + j * y * z, j * x + i * y, z)

def pow(x, y):
    if y == 1:
        return x
    tmp = pow(x, y // 2)
    tmp = mult(tmp, tmp)
    if y % 2 == 1:
        tmp = mult(tmp, x)
    return tmp

a, b, n, k = map(int, input().split())
x = (a, 1, b)
tmp = pow(x, n)
x, y, z = tmp # answer is x + y * sqrt(z)
print(tmp)
# print(str(int(tmp))[len(str(int(tmp))) - k])
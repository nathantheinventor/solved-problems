def mulMatrix(a, b):
    c,d,e,f = a
    
    g,h,i,j = b
    
    return c*g+d*i, c*h+d*j, e*g+f*i, e*h+f*j

def matrixPow(matrix, pow, mod):
    if pow == 1:
        return matrix
    tmp = matrixPow(matrix, pow // 2, mod)
    tmp = mulMatrix(tmp, tmp)
    if pow % 2 == 1:
        tmp = mulMatrix(tmp, matrix)
    tmp = list(tmp)
    for i in range(4):
        tmp[i] %= mod
    return tmp

for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    c,d,e,f = matrixPow([1, 1, 1, 0], n-1, 10 ** m)
    # print(c,d,e,f)
    print((c*b+d*a) % (10 ** m))
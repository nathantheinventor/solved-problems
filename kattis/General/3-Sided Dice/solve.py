def transposeMatrix(m):
    return [*map(list,zip(*m))]

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
    [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def dot(m1, m2):
    return [sum([a * b for a, b in zip(line, m2)]) for line in m1]

a, b, c = map(int, input().split())
while sum([a, b, c]) > 0:
    a2, b2, c2 = map(int, input().split())
    a3, b3, c3 = map(int, input().split())
    a4, b4, c4 = map(int, input().split())

    try:
        inverse = getMatrixInverse([
            [a,a2,a3],
            [b,b2,b3],
            [c,c2,c3]
        ])

        a5, b5, c5 = dot(inverse, [a4, b4, c4])
        if 0 < a5 < 1 and 0 < b5 < 1 and 0 < c5 < 1:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")

    input()
    a, b, c = map(int, input().split())
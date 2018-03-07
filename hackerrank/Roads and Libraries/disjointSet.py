partition = [-1] * n

def root(elem):
    tmp = []
    while partition[elem] >= 0:
        tmp.append(elem)
        elem = partition[elem]
    for i in tmp:
        partition[i] = elem
    return elem

def join(x, y):
    a, b = root(a), root(b)
    if a == b:
        return
    if partition[a] > partition[b]:
        partition[b] += partition[a]
        partition[a] = b
    else:
        partition[a] += partition[b]
        partition[b] = a

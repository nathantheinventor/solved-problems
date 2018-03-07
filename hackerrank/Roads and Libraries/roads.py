#!/bin/python3

import sys

def root(partition, elem):
    while partition[elem] >= 0:
        elem = partition[elem]
    return elem

def partitions(part):
    return part.count(-1)        

for _ in range(int(input())):
    s = input().split()
    if len(s) < 2:
        exit(0)
    n, m, cl, cr = map(int, s)
    part = [-1 for i in range(n)]
    for _ in range(m):
        s = input().split()
        city_1, city_2 = map(int, s)
        city_1 -= 1
        city_2 -= 1
        if root(part, city_2) != root(part, city_1):
            part[root(part, city_2)] = root(part, city_1)
        
    parts = partitions(part)
    # print(parts, cl, (n - parts), cr)
    if cl <= cr:
        print(cl * n)
        continue
    #print(part)
    print(parts * cl + (n - parts) * cr)
        

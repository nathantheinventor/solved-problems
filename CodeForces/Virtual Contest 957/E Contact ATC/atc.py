from collections import deque
n, w = map(int, input().split())
inp = [input() for _ in range(n)]

class plane:
    order = 0
    def __init__(self, s: str):
        self.x, self.v = map(int, s.split())
        self.order = plane.order
        plane.order += 1
    
    def __lt__(self, other):
        # print(self.x / (self.v + wind), other.x / (other.v + wind))
        # if sign(self.v + wind) * self.x * abs(other.v + wind) == sign(other.v + wind) * other.x * abs(self.v + wind):
        #     # print("equal")
        #     return sign(wind) * self.v >= sign(wind) * other.v
        result = abs(self.x) * abs(other.v + wind) < abs(other.x) * abs(self.v + wind)
        # print(result)
        return result
    
    def __le__(self, other):
        if "order" in dir(other):
            return self.order <= other.order
        return True
    
    def __repr__(self):
        return "{}".format(self.order)
    
class plane2:
    order = 0
    def __init__(self, s: str):
        self.x, self.v = map(int, s.split())
        self.order = plane.order
        plane.order += 1
    
    def __lt__(self, other):
        # print(self.x / (self.v + wind), other.x / (other.v + wind))
        if sign(self.v + wind) * self.x * abs(other.v + wind) == sign(other.v + wind) * other.x * abs(self.v + wind):
            # print("equal")
            return -sign(wind) * self.v >= -sign(wind) * other.v
        result = sign(self.v + wind) * self.x * abs(other.v + wind) < sign(other.v + wind) * other.x * abs(self.v + wind)
        # print(result)
        return result
    
    def __le__(self, other):
        if "order" in dir(other):
            return self.order <= other.order
        return True
    
    def __repr__(self):
        return "{}".format(self.order)


def sign(x):
    if x < 0:
        return -1
    return 1

class myInt(int):
    def __init__(self, val):
        pass
    def __le__(self, other):
        return False

def print_array(arr):
    l = len(arr)
    for i in range(l):
        print(arr[i], end = ' ')
    print()

def mergesort(arr, start, end):
    count = 0
    if start < end:
        mid = int((start + end - 1) / 2)
        count += mergesort(arr, start, mid)
        count += mergesort(arr, mid + 1, end)
        count += merge(arr, start, mid, end)
    return count
        
def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    left = [0] * n1
    right = [0] * n2
    for i in range(n1):
        left[i] = arr[start + i]
    for j in range(n2):
        right[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = start
    count = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
            #string = "i = " + str(i) + " j = " + str(j) + " mid = " + str(mid) + " n1 = " + str(n1)
            #print(string)
            count = count + n1 - i
        k = k + 1
    if i < n1:
        for m in range(i, n1):
            arr[k] = left[m]
            k = k + 1
    elif j < n2:
        for m in range(j, n2):
            arr[k] = right[m]
            k = k + 1
    return count

def getInvCount(arr, n):
    inv_count = 0
    for i in range(0, n - 1):
        for j in range(i+1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
 
    return inv_count

            
wind = 0
def solve1():
    global wind
    planes = [plane(s) for s in inp]
    wind = w
    order1 = sorted(planes)
    # print(order1)
    for i in range(n):
        order1[i].order = i
    wind = -w
    order2 = sorted(planes)
    
    # print(order2)
    
    order2 = [int(repr(x)) for x in order2]
    
    
    return (getInvCount(order2, n))

def solve2():
    global wind
    planes = [plane2(s) for s in inp]
    wind = w
    order1 = sorted(planes)
    # print(order1)
    for i in range(n):
        order1[i].order = i
    wind = -w
    order2 = sorted(planes)
    
    # print(order2)
    
    order2 = [int(repr(x)) for x in order2]
    
    
    return (getInvCount(order2, n))



print(max(solve1(), solve2()))
workout = [int(x) for x in input().split()]
neighbors = [[int(x) for x in input().split()] for i in range(10)]

currTime = 0

for i in range(3):
    for j in range(10):
        time, rest = workout[j * 2], workout[j * 2 + 1]
        u, r, t = neighbors[j]
        otherUser = (currTime - t) % (u + r)
        if currTime >= t and otherUser < u:
            #the other user is going to use it
            currTime += u - otherUser
            currTime += time
            if time > r:
                t = currTime
        else:
            #Jim is going to use it
            currTime += time
            if time > (u + r - otherUser) and currTime >= t:
                t = currTime
        #print("Jim started machine {} at time {}".format(j, currTime - time))
        neighbors[j][2] = t
        currTime += rest

print(currTime - workout[-1])
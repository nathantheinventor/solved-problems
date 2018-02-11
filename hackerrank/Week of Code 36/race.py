#!/bin/python3

import sys

def raceAgainstTime(n, mason_height, heights, prices):
    cost = 0
    costs = [(mason_height, 0)] # cost to get to this point, if we choose this node
    
    cur = mason_height
    
    tmpCost = 0
    
    lastBig = 0
    
    i = 0
    
    for h, p in zip(heights, prices):
        #calculate the cost if we were to choose this node
        thisCost = abs(h - cur) + cost + p
        #biggest item we've seen so far
        maxBelow = 0
        
        #iterate through what we've seen so far, backwards
        for h1, c in costs[::-1]:
            # if this is the biggest height we've seen so far
            if h1 >= maxBelow:
                
                # then see if this is the best price
                thisCost = min(thisCost, abs(h1 - h) + p + c)
                maxBelow = h1
        
        #print(thisCost, file=sys.stderr)
        # see if we have the best total price so far
        tmpCost = min(thisCost, tmpCost)
        while len(costs) > 0 and (costs[-1][0] < h or costs[-1][1] > thisCost + abs(costs[-1][0] - h)):
            del costs[-1]
        #print(costs[-1][0] - h, thisCost, costs[-1], h, len(costs), p)
        if len(costs) == 0 or thisCost - abs(costs[-1][0] - h) <= costs[-1][1]:
            costs.append((h, thisCost))
        
        
        if h >= cur:
            cost = thisCost
            tmpCost = cost
            cur = h
            lastBig = i
        
        i += 1
    
    return min([y for x, y in costs]) + n

if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    result = raceAgainstTime(n, mason_height, heights, prices)
    print(result)

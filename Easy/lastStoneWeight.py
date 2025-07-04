# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq

def lastStoneWeight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)
    
    while len(stones) > 1:
        heavyStone = -heapq.heappop(stones)
        secondHeavy = -heapq.heappop(stones)

        if (heavyStone != secondHeavy):
            heapq.heappush(stones, -(heavyStone - secondHeavy))
    
    return -stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))


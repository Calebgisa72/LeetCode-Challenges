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


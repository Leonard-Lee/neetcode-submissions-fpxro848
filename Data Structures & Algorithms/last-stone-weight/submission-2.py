class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: 
            return 0
        elif len(stones) == 1:
            return stones[0]

        stones = [-s for s in stones]

        # max heap
        pq = stones
        heapq.heapify(pq)
        while len(pq) > 1:
            max1 = heapq.heappop(pq)
            max2 = heapq.heappop(pq)
            if max2 > max1:
                heapq.heappush(pq, max2 - max1)
        
        stones.append(0)
        return pq[0]


        
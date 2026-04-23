class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        elif len(stones) == 1:
            return stones[0]

        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            max1 = heapq.heappop(maxHeap) * -1 # become positive
            max2 = heapq.heappop(maxHeap) * -1
            if max1 - max2 > 0:
                heapq.heappush(maxHeap, max2 - max1)

        if not maxHeap:
            return 0
        return maxHeap[0] * -1
        
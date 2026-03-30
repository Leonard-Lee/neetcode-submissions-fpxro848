class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        
        for key, val in count.items():
            heapq.heappush(heap, (val, key))

        while len(heap) > k:
            heapq.heappop(heap)

        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret
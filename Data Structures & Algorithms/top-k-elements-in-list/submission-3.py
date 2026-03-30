class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # klogn
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap =[]
        for key, freq in count.items():
            heapq.heappush(heap, (freq, key))

        while (len(heap) > k):
            heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        
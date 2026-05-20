class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        minHeap = []

        for num in nums:
            freqMap[num] += 1

        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for freq, num in minHeap:
            res.append(num)

        return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1

        minHeap = []
        for key, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for freq, key in minHeap:
            res.append(key)

        return res
        
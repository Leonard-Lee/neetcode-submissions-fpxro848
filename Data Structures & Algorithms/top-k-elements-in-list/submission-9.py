class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1

        minHeap = []
        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for freq, num in minHeap:
            res.append(num)

        return res


        
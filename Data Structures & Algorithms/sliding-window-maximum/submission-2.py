class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []

        l = 0
        for r in range(len(nums)):
            heapq.heappush(pq, (-nums[r], r))

            if r - l + 1 >= k:
                while pq[0][1] < l:
                    heapq.heappop(pq)
                res.append(-pq[0][0])
        return res

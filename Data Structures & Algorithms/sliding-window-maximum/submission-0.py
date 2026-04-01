class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []

        l = 0;
        pq = []
        res = []
        mem = {}
        for r in range(len(nums)):
            heapq.heappush(pq, -nums[r])
            if r - l + 1 >= k:
                max = -pq[0]
                res.append(max)
                if pq[l] == max:
                    heapq.heappop(pq)
                    
                l += 1

        return res






        
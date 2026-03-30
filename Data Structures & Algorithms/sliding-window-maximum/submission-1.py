class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # idx
        l = r = 0

        while r < len(nums):
            # pop smaller values from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                max = nums[q[0]]
                res.append(max)
                l += 1

            r += 1
        return res

        
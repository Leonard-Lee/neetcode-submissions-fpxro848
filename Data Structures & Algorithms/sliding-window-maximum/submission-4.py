class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # index
        res = []

        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r + 1 >= k:
                if l > q[0]:
                    q.popleft()
                l += 1
                res.append(nums[q[0]])

            r += 1

        return res
        
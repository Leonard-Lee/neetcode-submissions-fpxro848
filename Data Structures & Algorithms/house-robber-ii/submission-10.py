# To handle the circular neighborhood, we split the problem into two linear sub-problems:
# 1. Skip the last house entirely. This gives the algorithm permission to safely evaluate the first house.
# 2. Skip the first house entirely. This catches any missed opportunities by giving the algorithm permission to safely evaluate the last house.
# The optimal combination is guaranteed to be the max of these two passes.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        # n = len(nums)
        # memo = {}
        # def dfs(idx, end) -> int:
        #     if (idx, end) in memo:
        #         return memo[(idx, end)]

        #     if idx >= end:
        #         memo[(idx, end)] = 0
        #         return 0

        #     memo[(idx, end)] = max(dfs(idx + 1, end), nums[idx] + dfs(idx + 2, end))
        #     return memo[(idx, end)]  

        # return max(dfs(0, n - 1), dfs(1, n))

        def helper(nums) -> int:
            if not nums:
                return 0
            
            if len(nums) == 1:
                return nums[0]
                
            n = len(nums)
            res = [0] * n
            res[0] = nums[0]
            res[1] = max(nums[0], nums[1])

            for i in range(2, n):
                res[i] = max(res[i - 1], nums[i] + res[i - 2])

            return res[-1]
                
        return max(helper(nums[1:]), helper(nums[:-1]))






        
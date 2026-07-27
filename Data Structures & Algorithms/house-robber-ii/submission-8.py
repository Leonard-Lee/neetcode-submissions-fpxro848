class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo = {}
        def dfs(idx, end) -> int:
            if (idx, end) in memo:
                return memo[(idx, end)]

            if idx >= end:
                memo[(idx, end)] = 0
                return 0

            memo[(idx, end)] = max(dfs(idx + 1, end), nums[idx] + dfs(idx + 2, end))
            return memo[(idx, end)]  

        return max(dfs(0, n - 1), dfs(1, n))



        
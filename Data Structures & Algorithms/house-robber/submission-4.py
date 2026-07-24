class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # memo = {}
        # def dfs(idx) -> int:
        #     if idx in memo:
        #         return memo[idx]

        #     if idx >= len(nums):
        #         memo[idx] = 0
        #         return 0

        #     memo[idx] = max(dfs(idx + 1), nums[idx] + dfs(idx + 2))
        #     return memo[idx]

        # return dfs(0)

        n = len(nums)
        memo = [0] * (n + 2)
        for i in range(n):
            memo[i + 2] = max(memo[i + 1], memo[i] + nums[i])

        return memo[n + 1]
        
        
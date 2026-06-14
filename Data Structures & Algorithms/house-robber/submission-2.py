class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(idx: int) -> int:
            if idx >= len(nums):
                return 0

            if idx in dp:
                return dp[idx]

            res = nums[idx] + dfs(idx + 2)
            dp[idx] = max(res, dfs(idx + 1))

            return dp[idx]

        dfs(0)
        return dp[0]
            

        
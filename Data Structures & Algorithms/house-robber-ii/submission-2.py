class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        elif n == 1:
            return nums[0]

        dp = {}
        def dfs(idx: int, end: int) -> int:
            if idx > end:
                return 0

            if idx in dp:
                return dp[idx]

            res = nums[idx] + dfs(idx + 2, end)
            res = max(res, dfs(idx + 1, end))
            dp[idx] = res
            return dp[idx]

        res = dfs(0, n - 2)
        dp = {}
        return max(res, dfs(1, n -1))
        
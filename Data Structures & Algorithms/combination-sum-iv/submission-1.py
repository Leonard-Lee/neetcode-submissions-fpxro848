class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        dp = {}
        dp[target] = 1
        def dfs(total: int) -> int:
            if total > target:
                return 0

            if total in dp:
                return dp[total]

            count = 0
            for i in range(len(nums)):
                count += dfs(nums[i] + total)
                
            dp[total] = count 
            return dp[total]

        return dfs(0)
        
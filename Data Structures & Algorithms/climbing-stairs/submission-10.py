class Solution:
    def climbStairs(self, n: int) -> int:

        # dp = {}
        # def dfs(n) -> int:
        #     if n in dp:
        #         return dp[n]

        #     if n == 0:
        #         dp[n] = 1
        #         return 1
        #     elif n < 0:
        #         dp[n] = 0
        #         return 0

        #     dp[n] = dfs(n - 2) + dfs(n - 1)
        #     return dp[n]

        # return dfs(n)
        
        # bottom-up
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
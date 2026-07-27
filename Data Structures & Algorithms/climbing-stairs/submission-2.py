class Solution:
    def climbStairs(self, n: int) -> int:

        # n means stairs, it will return ways
        memo = {}
        memo[0] = 1
        memo[1] = 1
        def dfs(n) -> int:
            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)
        
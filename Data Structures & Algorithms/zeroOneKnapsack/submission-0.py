class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m = len(weight)
        n = capacity
        dp = [[0] * (n + 1) for i in range(m)]

        for c in range(n + 1):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for r in range(1, m):
            for c in range(1, n + 1):
                skip = dp[r - 1][c]
                include = 0
                if c >= weight[r]:
                    include = profit[r] + dp[r - 1][c - weight[r]]

                dp[r][c] = max(skip, include)

        return dp[m - 1][n]




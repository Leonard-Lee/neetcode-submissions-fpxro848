class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m = len(weight)
        n = capacity
        dp = [0] * (n + 1) 

        for c in range(n + 1):
            if c >= weight[0]:
                dp[c] = profit[0]

        for r in range(1, m):
            # Iterate backwards! You can also stop early at weight[r]
            # since anything smaller won't fit the current item anyway.
            for c in range(n, weight[r] - 1, -1):
                skip = dp[c]
                include = profit[r] + dp[c - weight[r]]
                dp[c] = max(skip, include)

        return dp[n]




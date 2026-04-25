class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
        
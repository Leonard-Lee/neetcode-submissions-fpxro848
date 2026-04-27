class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # default val
        for r in range(m):
            dp[r][n] = m - r

        for c in range(n):
            dp[m][c] = n - c


        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], min(dp[r][c + 1], dp[r + 1][c + 1]))

        return dp[0][0]
        
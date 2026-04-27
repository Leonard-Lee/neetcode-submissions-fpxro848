class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [0 for _ in range(n + 1)] 
        # default val
        for c in range(n):
            dp[c] = n - c


        for r in range(m - 1, -1, -1):
            nxt_dp = [0] * (n + 1)
            nxt_dp[n] = m - r
            for c in range(n - 1, -1, -1):
                if word1[r] == word2[c]:
                    nxt_dp[c] = dp[c + 1]
                else:
                    nxt_dp[c] = 1 + min(dp[c], min(nxt_dp[c + 1], dp[c + 1]))
            dp = nxt_dp

        return dp[0]
        
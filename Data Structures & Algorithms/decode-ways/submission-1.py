class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        dp[n] = 1

        def dfs(idx: int) -> int:
            if idx in dp:
                return dp[idx]

            if s[idx] == "0":
                return 0

            dp[idx] = dfs(idx + 1)
            if (idx + 1 < len(s)) and ((s[idx] == "1") or (s[idx] == "2" and s[idx + 1] < "7")):
                dp[idx] += dfs(idx + 2)

            return dp[idx]
        return dfs(0)

        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = {}
        dp[n] = True

        def dfs(idx: int) -> bool:
            if idx in dp:
                return dp[idx]

            dp[idx] = False
            for i in range(idx, n):
                if s[idx: i + 1] in wordSet and dfs(i + 1):
                    dp[idx] = True
                    break

            return dp[idx]

        return dfs(0)
        
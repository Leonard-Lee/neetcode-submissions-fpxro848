class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = {}
        dp[n] = True
        # this is the key
        max_len = max(len(w) for w in wordDict)

        def dfs(idx: int) -> bool:
            if idx in dp:
                return dp[idx]

            dp[idx] = False
            for i in range(idx, min(n, idx + max_len)):
                if s[idx: i + 1] in wordSet and dfs(i + 1):
                    dp[idx] = True
                    break

            return dp[idx]

        return dfs(0)
        
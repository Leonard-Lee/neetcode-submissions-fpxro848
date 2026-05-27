class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        n = len(s)
        # build dp
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        res = []
        cur = []
        def dfs(idx: int) -> None:
            if idx == n:
                res.append(cur.copy())
                return

            for j in range(idx, n):
                if dp[idx][j]:
                    cur.append(s[idx: j + 1])
                    dfs(j + 1)
                    cur.pop()

        dfs(0)
        return res

    # def isPalin(self, s: str, i: int, j: int) -> bool:
    #     while i < j:
    #         if s[i] != s[j]:
    #             return False

    #         i += 1
    #         j -= 1
    #     return True

        
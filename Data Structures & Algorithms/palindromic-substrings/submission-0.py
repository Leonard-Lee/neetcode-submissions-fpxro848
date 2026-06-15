class Solution:
    def countSubstrings(self, s: str) -> int:
        if not str:
            return 0

        res = 0
        n = len(s)

        for idx in range(n):
            i, j = idx, idx
            while i >= 0 and j < n and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1

        for idx in range(n - 1):
            i, j = idx, idx + 1
            while i >= 0 and j < n and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1

        return res

        
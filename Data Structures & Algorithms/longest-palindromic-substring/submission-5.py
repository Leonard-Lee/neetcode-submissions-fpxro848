class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ""

        if not s:
            return maxStr

        n = len(s)
        for idx in range(n):
            i, j = idx, idx
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 > len(maxStr):
                    maxStr = s[i: j + 1]
                i -= 1
                j += 1

        for idx in range(n - 1):
            i, j = idx, idx + 1
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 > len(maxStr):
                    maxStr = s[i: j + 1]
                i -= 1
                j += 1

        return maxStr
        
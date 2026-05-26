class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ""

        for idx in range(len(s)):
            i, j = idx, idx
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > len(maxStr):
                    maxStr = s[i: j + 1]

                i -= 1
                j += 1

            i, j = idx, idx + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > len(maxStr):
                    maxStr = s[i: j + 1]

                i -= 1
                j += 1

        return maxStr
            
        
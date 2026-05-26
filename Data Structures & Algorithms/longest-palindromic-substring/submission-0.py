class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ""

        for i in range(len(s)):
            substr = self.findPalindrome(s, i)
            substr2 = self.findPalindrome2(s, i)
            if len(substr) > len(maxStr):
                maxStr = substr

            if len(substr2) > len(maxStr):
                maxStr = substr2

        return maxStr

    def findPalindrome(self, s: str, idx: int) -> str:
        i, j = idx - 1, idx + 1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break

            i -= 1
            j += 1

        return s[i + 1: j]
        
    def findPalindrome2(self, s: str, idx: int) -> str:
        i, j = idx, idx + 1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break

            i -= 1
            j += 1

        return s[i + 1: j]
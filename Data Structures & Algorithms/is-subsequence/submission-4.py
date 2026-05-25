class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            return False

        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            while j < n and s[i] != t[j]:
                j += 1  
            j += 1
            i += 1

        return i == m
            
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1: return True

        chars = list(s.lower())
        i, j = 0, len(chars) - 1
        while i < j:
            if not self.isAlphaNum(chars[i]): 
                i += 1
                continue
            
            if not self.isAlphaNum(chars[j]): 
                j -= 1
                continue

            if chars[i] != chars[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')) 


        
        
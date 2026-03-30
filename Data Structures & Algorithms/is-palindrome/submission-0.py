class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1: return True

        chars = list(s.lower())
        i, j = 0, len(chars) - 1
        while i < j:
            if not chars[i].isalnum(): 
                i += 1
                continue
            
            if not chars[j].isalnum(): 
                j -= 1
                continue

            if chars[i] != chars[j]:
                return False
            else:
                i += 1
                j -= 1
        return True



        
        
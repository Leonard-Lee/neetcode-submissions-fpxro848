class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        l = 0
        count2 = {}
        for r, c in enumerate(s2):
            count2[c] = count2.get(c, 0) + 1 

            while (l <= r) and (c not in count1 or count2[c] > count1[c]):
                count2[s2[l]] = count2[s2[l]] - 1 
                l = l + 1
            
            if r - l + 1 == len(s1):
                return True

        return False
        
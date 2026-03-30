class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
        
        l = 0
        s2Count = {}
        for r in range(len(s2)):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1 

            while (l <= r) and (s2[r] not in s1Count or s2Count[s2[r]] > s1Count[s2[r]]):
                s2Count[s2[l]] = s2Count[s2[l]] - 1 
                l = l + 1
            
            if r - l + 1 == len(s1):
                return True

        return False
        
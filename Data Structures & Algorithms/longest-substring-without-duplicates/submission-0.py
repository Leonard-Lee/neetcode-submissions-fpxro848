class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = 0
        l, r = 0, 0
        mem = set()
        while r < len(s):
            if s[r] not in mem:
                mem.add(s[r])
                maxSize = max(maxSize, r - l + 1)
                r += 1
            else:
                mem.remove(s[l])
                l += 1

        return maxSize
            
        
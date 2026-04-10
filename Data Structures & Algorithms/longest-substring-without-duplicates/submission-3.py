class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # num : idx + 1
        map = {}
        maxLen = 0
        i = 0
        for j in range(len(s)):
            ch = s[j]
            if ch not in map:
                map[ch] = j + 1
            else:
                i = max(map[ch], i)
                map[ch] = j + 1
            maxLen = max(maxLen, j - i + 1)

        return maxLen
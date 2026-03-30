class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not str: return 0

        l, r = 0, 0
        freq = {}
        maxFreq = 0
        res = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            while r - l + 1 - maxFreq > k:
                freq[s[l]] = freq[s[l]] - 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res


        
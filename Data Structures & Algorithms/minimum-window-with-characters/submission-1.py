class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        requiredCount = {}
        for c in t:
            requiredCount[c] = requiredCount.get(c, 0) + 1

        requiredLen = len(requiredCount)

        windowLen, window = 0, defaultdict(int)
        l = 0
        best = (l, float("inf"))
        for r, c in enumerate(s):
            window[c] += 1

            if c in requiredCount and window[c] == requiredCount[c]:
                windowLen += 1

            while windowLen == requiredLen:
                if r - l + 1 < best[1]:
                    best = (l, r - l + 1)
                left_ch = s[l]
                window[left_ch] -= 1
                l += 1

                if left_ch in requiredCount and window[left_ch] < requiredCount[left_ch]:
                    windowLen -= 1
                
        if best[1] == float("inf"):
                return ""

        l, length = best
        return s[l:l + length]

        
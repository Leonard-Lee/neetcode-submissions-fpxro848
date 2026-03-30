class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        required = len(need)

        window = defaultdict(int)
        formed = 0

        l = 0
        best = (0, float("inf"))
        for r, ch in enumerate(s):
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if (r - l + 1) < best[1]:
                    best = (l, r - l + 1)

                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                l += 1 
        
        if best[1] == float("inf"):
            return ""
        
        l, length = best
        return s[l: l + length]
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        res = []
        sub = []

        def helper(idx):
            if idx >= len(s):
                res.append(sub.copy())
                return

            for j in range(idx, len(s)):
                substr = s[idx: j + 1]
                if self.isPalin(substr):
                    sub.append(substr)
                    helper(j + 1)
                    sub.pop()

        helper(0)
        return res

    def isPalin(self, s):
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def dfs(idx: int) -> None:
            if idx == len(s):
                res.append(cur.copy())
                return

            for j in range(idx, len(s)):
                if self.isPalin(s, idx, j):
                    cur.append(s[idx: j + 1])
                    dfs(j + 1)
                    cur.pop()

        dfs(0)
        return res

    def isPalin(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
            
        return True
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

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

    def isPalin(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True

        
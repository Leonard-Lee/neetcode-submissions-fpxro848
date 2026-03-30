class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        res = []
        cur = []

        def helper(idx):
            if len(cur) == k:
                res.append(cur.copy())
                return

            for i in range(idx, n + 1):
                cur.append(i)
                helper(i + 1)
                cur.pop()

        helper(1)
        return res
        
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def helper(idx):
            # base case
            if len(cur) == k:
                res.append(cur.copy())
                return

            for j in range(idx, n + 1):
                cur.append(j)
                helper(j + 1)
                cur.pop()

        helper(1)
        return res
            

        
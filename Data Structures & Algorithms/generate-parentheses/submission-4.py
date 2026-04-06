class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []


        res = []
        cur = []
        def helper(l, r):
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return

            if l < n:
                cur.append("(")
                helper(l + 1, r)
                cur.pop()

            if r < l:
                cur.append(")")
                helper(l , r + 1)
                cur.pop()

        helper(0, 0)
        return res
        
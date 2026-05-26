class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        # l means left parenthese
        # r means right parenthese
        def helper(l: int, r: int) -> None:
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return

            if l < n:
                cur.append("(")
                helper(l + 1, r)
                cur.pop()

            if r < l:
                cur.append(")")
                helper(l, r + 1)
                cur.pop()

        helper(0, 0)
        return res
        
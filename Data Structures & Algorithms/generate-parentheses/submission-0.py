class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def helper(left, right):
            if right > left:
                return
            elif len(cur) == 2 * n:
                if right == left:
                    res.append("".join(cur))
                return

            cur.append("(") 
            helper(left + 1, right)
            cur.pop()
            cur.append(")") 
            helper(left, right + 1)
            cur.pop()

        helper(0, 0)
        return res
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def helper(left, right):
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return

            if left < n:
                cur.append("(") 
                helper(left + 1, right)
                cur.pop()
            
            if right < left:
                cur.append(")") 
                helper(left, right + 1)
                cur.pop()

        helper(0, 0)
        return res
        
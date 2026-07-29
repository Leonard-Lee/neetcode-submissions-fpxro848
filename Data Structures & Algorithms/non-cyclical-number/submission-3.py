class Solution:
    def isHappy(self, n: int) -> bool:

        def sumSquareDigit(n: int) -> int:
            res = 0
            while n:
                res += (n % 10) ** 2
                n = n // 10
            return res

        visitSet = set()
        while n not in visitSet:
            visitSet.add(n)
            n = sumSquareDigit(n)
            if n == 1:
                return True

        return False
        
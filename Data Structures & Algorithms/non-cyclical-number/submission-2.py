class Solution:
    def isHappy(self, n: int) -> bool:

        def sumSquareDigit(n: int) -> int:
            res = 0
            while n:
                res += (n % 10) ** 2
                n = n // 10
            return res

        visitSet = set()
        while n != 1 or n in visitSet:
            n = sumSquareDigit(n)
            print(n)
            if n == 1:
                return True
            else:
                if n in visitSet:
                    return False
                else:
                    visitSet.add(n)

        return True if n == 1 else False
        
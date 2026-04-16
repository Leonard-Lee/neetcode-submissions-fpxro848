class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x

        num = self.myPow(x, n // 2)
        res = 0
        if n % 2 == 0:
            res = num * num
        else:
            res = x * num * num

        return res

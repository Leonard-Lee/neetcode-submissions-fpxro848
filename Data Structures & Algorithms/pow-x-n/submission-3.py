class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -n)

        num = self.myPow(x, n // 2)
        if n % 2 == 0:
            return num * num
        else:
            return x * num * num
        
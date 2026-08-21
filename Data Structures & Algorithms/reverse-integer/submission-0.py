class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        sign = 1 if x >= 0 else -1 

        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > 7):
                return 0
            

            res = res * 10 + digit

        return res * sign


        
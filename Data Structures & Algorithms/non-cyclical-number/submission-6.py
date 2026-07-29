class Solution:
    def isHappy(self, n: int) -> bool:

        def sumSquareDigit(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output

        slow, fast = n, sumSquareDigit(n)
        while slow != fast:
            if slow == 1 or fast == 1:
                return True

            slow = sumSquareDigit(slow)
            fast = sumSquareDigit(sumSquareDigit(fast)) 

        return True if fast == 1 else False
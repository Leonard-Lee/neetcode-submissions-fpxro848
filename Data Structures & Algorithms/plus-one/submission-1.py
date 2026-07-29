class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return 0

        res = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            else:
                carry = 0

            res.append(digits[i])

        if carry:
            res.append(carry)

        res.reverse()
        return res
        
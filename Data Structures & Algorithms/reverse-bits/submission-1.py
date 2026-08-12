class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            
            if n & 1:
                res += 1
            if i < 31:
                res = res << 1
            n = n >> 1

        return res
        
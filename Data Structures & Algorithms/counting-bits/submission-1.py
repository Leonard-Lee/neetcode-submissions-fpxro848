class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
            
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            if i % 2:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp
        
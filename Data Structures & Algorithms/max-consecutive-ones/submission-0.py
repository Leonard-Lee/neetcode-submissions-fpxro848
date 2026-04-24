class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxRes = 0

        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                maxRes = max(maxRes, cur)
            else:
                cur = 0

        return maxRes

        
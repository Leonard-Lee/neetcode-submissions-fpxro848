class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        res = [0] * 2 * n

        for i in range(len(res)):
            res[i] = nums[i % n]

        return res
        
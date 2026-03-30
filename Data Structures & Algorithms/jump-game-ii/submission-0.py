class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        count = 0
        while r < len(nums) - 1:
            minVal = l
            maxVal = r
            for i in range(l, r + 1):
                if nums[i] > 0:
                    minVal = min(minVal, i + 1)

                maxVal = max(maxVal, i + nums[i])
            l = minVal
            r = maxVal
            count += 1

        return count

        
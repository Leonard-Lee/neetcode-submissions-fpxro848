class Solution:
    def check(self, nums: List[int]) -> bool:
        if not nums:
            return False

        drops = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                drops += 1

        return drops <= 1
        
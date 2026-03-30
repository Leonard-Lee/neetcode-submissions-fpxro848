class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        right = len(nums) - 1
        left = 0
        while left <= right:
            n = (left + right) // 2
            print(n)
            if nums[n] > target:
                right = n - 1
            elif nums[n] < target:
                left = n + 1
            else:
                return n
        return -1

        